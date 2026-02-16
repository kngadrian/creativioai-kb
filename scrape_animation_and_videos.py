#!/usr/bin/env python3
"""
Scrape Animation Studio styles and search for Vimeo videos across the app
"""

from playwright.sync_api import sync_playwright
import time
import json
import re
import os

def login(page):
    """Log into CreativioAI"""
    print("🔐 Logging in...")
    page.goto('https://v2.creativio.ai/login', wait_until='networkidle')
    time.sleep(2)
    
    page.fill('input[type="email"]', 'jackson@creativio.com')
    page.click('input[type="password"]')
    page.type('input[type="password"]', 'lNh$@uW3Hj7aZXmv')
    page.click('button[type="submit"]')
    time.sleep(8)
    
    print("✅ Logged in")
    return True

def extract_vimeo_urls(html):
    """Extract Vimeo URLs from HTML"""
    vimeo_patterns = [
        r'https://player\.vimeo\.com/video/(\d+)',
        r'vimeo\.com/video/(\d+)',
        r'player\.vimeo\.com/video/(\d+)',
        r'vimeo\.com/(\d+)'
    ]
    
    all_ids = []
    for pattern in vimeo_patterns:
        matches = re.findall(pattern, html)
        all_ids.extend(matches)
    
    # Deduplicate
    unique_ids = list(set(all_ids))
    return [f"https://player.vimeo.com/video/{vid}" for vid in unique_ids]

def search_for_videos_everywhere(page, screenshot_dir):
    """Navigate through the app looking for videos"""
    print("\n🔍 Searching for videos across the app...")
    
    all_vimeo_urls = []
    
    # Check current page
    html = page.content()
    vimeo_urls = extract_vimeo_urls(html)
    if vimeo_urls:
        print(f"  Found {len(vimeo_urls)} Vimeo URLs on current page")
        all_vimeo_urls.extend(vimeo_urls)
    
    # Try to navigate to different sections and check for videos
    sections_to_check = [
        ('text="Training"', 'training'),
        ('text="Video Training"', 'video-training'),
        ('text="Tutorials"', 'tutorials'),
        ('text="Help"', 'help'),
        ('text="Learn"', 'learn'),
        ('text="Getting Started"', 'getting-started'),
        ('a:has-text("Video")', 'video-link'),
        ('button:has-text("Tutorial")', 'tutorial-button'),
    ]
    
    for selector, name in sections_to_check:
        try:
            element = page.locator(selector).first
            if element.count() > 0:
                print(f"  Checking section: {name}")
                element.click()
                time.sleep(3)
                
                # Take screenshot
                page.screenshot(path=f"{screenshot_dir}/section-{name}.png")
                
                # Check for videos
                html = page.content()
                vimeo_urls = extract_vimeo_urls(html)
                if vimeo_urls:
                    print(f"    ✅ Found {len(vimeo_urls)} Vimeo URLs!")
                    all_vimeo_urls.extend(vimeo_urls)
                    
                    # Save HTML
                    with open(f"{screenshot_dir}/section-{name}.html", 'w') as f:
                        f.write(html)
                
                # Go back
                page.goto('https://v2.creativio.ai', wait_until='networkidle')
                time.sleep(2)
        except Exception as e:
            print(f"    Could not access {name}: {e}")
            continue
    
    # Deduplicate all URLs
    all_vimeo_urls = list(set(all_vimeo_urls))
    return all_vimeo_urls

def scrape_animation_studio_styles(page, screenshot_dir):
    """Navigate to Animation Studio and extract all animation styles"""
    print("\n🎬 Scraping Animation Studio styles...")
    
    try:
        # Navigate to Animation Studio
        for selector in ['text="Animation Studio"', 'a:has-text("Animation")', 'button:has-text("Animation")']:
            try:
                element = page.locator(selector).first
                if element.count() > 0:
                    print(f"  Clicking: {selector}")
                    element.click()
                    time.sleep(3)
                    break
            except:
                continue
        
        # Take screenshot
        page.screenshot(path=f"{screenshot_dir}/animation-studio-full.png", full_page=True)
        
        # Save HTML
        html = page.content()
        with open(f"{screenshot_dir}/animation-studio.html", 'w') as f:
            f.write(html)
        
        print(f"  📸 Screenshot and HTML saved")
        
        # Look for style/template selectors
        # Try to find and click on style dropdown or buttons
        style_selectors = [
            'text="Style"',
            'text="Template"', 
            'text="Effect"',
            'text="Animation"',
            'button:has-text("Style")',
            'select',
            '[class*="style"]',
            '[class*="template"]'
        ]
        
        for selector in style_selectors:
            try:
                element = page.locator(selector)
                count = element.count()
                if count > 0:
                    print(f"  Found {count} elements matching: {selector}")
                    
                    # Click the first one
                    element.first.click()
                    time.sleep(2)
                    
                    # Take screenshot of opened selector
                    page.screenshot(path=f"{screenshot_dir}/animation-styles-opened.png")
                    
                    # Save HTML
                    html = page.content()
                    with open(f"{screenshot_dir}/animation-styles.html", 'w') as f:
                        f.write(html)
                    
                    print(f"  ✅ Captured styles view")
                    break
            except Exception as e:
                print(f"  Could not interact with {selector}: {e}")
                continue
        
        # Extract style names from HTML
        # Look for patterns similar to Create Photoshoot
        styles = []
        
        # Try to extract style names from the HTML
        style_name_patterns = [
            r'<h[3-5][^>]*>([^<]+)</h[3-5]>',
            r'data-style="([^"]+)"',
            r'class="[^"]*style-name[^"]*">([^<]+)<',
        ]
        
        for pattern in style_name_patterns:
            matches = re.findall(pattern, html)
            if matches:
                print(f"  Found {len(matches)} potential style names with pattern: {pattern[:50]}")
                styles.extend(matches)
        
        # Deduplicate
        styles = list(set([s.strip() for s in styles if s.strip() and len(s) < 100]))
        
        return styles
        
    except Exception as e:
        print(f"  ❌ Error: {e}")
        import traceback
        traceback.print_exc()
        return []

def main():
    screenshot_dir = "static/img/screenshots"
    os.makedirs(screenshot_dir, exist_ok=True)
    
    results = {
        'vimeo_urls': [],
        'animation_styles': []
    }
    
    with sync_playwright() as p:
        print("🚀 Launching browser...")
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(viewport={'width': 1920, 'height': 1080})
        page = context.new_page()
        
        # Login
        if not login(page):
            print("❌ Login failed")
            return
        
        time.sleep(3)
        
        # Search for Vimeo videos
        vimeo_urls = search_for_videos_everywhere(page, screenshot_dir)
        results['vimeo_urls'] = vimeo_urls
        
        # Go back to dashboard
        page.goto('https://v2.creativio.ai', wait_until='networkidle')
        time.sleep(2)
        
        # Scrape Animation Studio
        animation_styles = scrape_animation_studio_styles(page, screenshot_dir)
        results['animation_styles'] = animation_styles
        
        # Save results
        with open('animation_and_videos.json', 'w') as f:
            json.dump(results, f, indent=2)
        
        print("\n" + "="*60)
        print("📊 SCRAPING COMPLETE")
        print("="*60)
        print(f"Vimeo URLs found: {len(results['vimeo_urls'])}")
        print(f"Animation styles found: {len(results['animation_styles'])}")
        
        if results['vimeo_urls']:
            print("\n📹 Vimeo Videos:")
            for url in results['vimeo_urls']:
                print(f"  • {url}")
        
        if results['animation_styles']:
            print("\n🎬 Animation Styles:")
            for style in sorted(results['animation_styles'])[:30]:  # Show first 30
                print(f"  • {style}")
        
        print(f"\nResults saved to: animation_and_videos.json")
        
        browser.close()

if __name__ == "__main__":
    main()
