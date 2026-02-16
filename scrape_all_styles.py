#!/usr/bin/env python3
"""
Enhanced script to click through ALL style categories and extract complete info
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

def extract_styles_from_html(html):
    """Extract style information from HTML"""
    styles = []
    
    # Pattern to match style cards
    style_pattern = r'<h5[^>]*>([^<]+)</h5>\s*<p[^>]*>([^<]+)</p>.*?Perfect for:\s*([^<]+)</span>'
    matches = re.findall(style_pattern, html, re.DOTALL)
    
    for match in matches:
        name = match[0].strip()
        description = match[1].strip().replace('&amp;', '&')
        use_case = match[2].strip()
        
        styles.append({
            'name': name,
            'description': description,
            'use_case': use_case
        })
    
    return styles

def scrape_all_photoshoot_styles(page, screenshot_dir):
    """Navigate to Create Photoshoot and extract ALL styles from ALL categories"""
    print("\n🎨 Scraping ALL Create Photoshoot styles...")
    
    all_styles = []
    categories_info = {}
    
    try:
        # Navigate to Create Photoshoot
        print("Navigating to Create Photoshoot...")
        
        # Try to find and click Create Photoshoot
        for selector in ['text="Create Photoshoot"', 'a:has-text("Photoshoot")', 'button:has-text("Create")']:
            try:
                element = page.locator(selector).first
                if element.count() > 0:
                    element.click()
                    time.sleep(3)
                    break
            except:
                continue
        
        # Take initial screenshot
        page.screenshot(path=f"{screenshot_dir}/photoshoot-initial.png")
        
        # Find all category buttons
        # Look for buttons that have category names and style counts
        # Based on the HTML, categories are in buttons with specific text patterns
        
        category_selectors = [
            'text="Product & E-Commerce"',
            'text="Brand & Marketing"', 
            'text="Cinematic & Editorial"',
            'text="Creative & Trending"'
        ]
        
        category_index = 0
        
        for category_selector in category_selectors:
            try:
                print(f"\n📂 Processing category: {category_selector}")
                
                # Click the category to expand it
                category_button = page.locator(category_selector).first
                
                if category_button.count() > 0:
                    category_button.click()
                    time.sleep(2)
                    
                    # Get the category name
                    category_name = category_selector.replace('text="', '').replace('"', '')
                    
                    # Take screenshot of expanded category
                    page.screenshot(path=f"{screenshot_dir}/category-{category_index}-{category_name.replace(' ', '-').replace('&', 'and').lower()}.png")
                    
                    # Extract styles from the current HTML
                    html = page.content()
                    
                    # Save HTML for this category
                    with open(f"{screenshot_dir}/category-{category_index}.html", 'w') as f:
                        f.write(html)
                    
                    # Parse styles
                    styles = extract_styles_from_html(html)
                    
                    print(f"   Found {len(styles)} styles in this category")
                    
                    for style in styles:
                        # Add category to style info
                        style['category'] = category_name
                        
                        # Avoid duplicates
                        if not any(s['name'] == style['name'] for s in all_styles):
                            all_styles.append(style)
                            print(f"   ✓ {style['name']}")
                    
                    categories_info[category_name] = len(styles)
                    
                    category_index += 1
                    
                    # Click again to collapse (optional)
                    # category_button.click()
                    # time.sleep(1)
                else:
                    print(f"   ⚠️  Category button not found: {category_selector}")
                    
            except Exception as e:
                print(f"   ❌ Error processing category {category_selector}: {e}")
                continue
        
        return all_styles, categories_info
        
    except Exception as e:
        print(f"❌ Error in scrape_all_photoshoot_styles: {e}")
        import traceback
        traceback.print_exc()
        return all_styles, categories_info

def main():
    screenshot_dir = "static/img/screenshots"
    os.makedirs(screenshot_dir, exist_ok=True)
    
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
        
        # Scrape all styles
        all_styles, categories = scrape_all_photoshoot_styles(page, screenshot_dir)
        
        # Save results
        result = {
            'total_styles': len(all_styles),
            'categories': categories,
            'styles': all_styles
        }
        
        with open('all_photoshoot_styles.json', 'w') as f:
            json.dump(result, f, indent=2)
        
        print("\n" + "="*60)
        print("📊 SCRAPING COMPLETE")
        print("="*60)
        print(f"Total styles extracted: {len(all_styles)}")
        print(f"Categories: {len(categories)}")
        print(f"\nResults saved to: all_photoshoot_styles.json")
        print(f"Screenshots in: {screenshot_dir}/")
        
        # Print summary by category
        print("\n📁 Styles by category:")
        for category, count in categories.items():
            print(f"  • {category}: {count} styles")
        
        browser.close()

if __name__ == "__main__":
    main()
