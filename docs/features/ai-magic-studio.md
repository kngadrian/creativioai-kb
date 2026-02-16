---
title: AI Magic Studio
sidebar_position: 4
---

# AI Magic Studio

AI Magic Studio is a canvas-based compositing editor that lets you combine images, apply AI effects, mask regions, and create professional compositions from multiple elements.

![AI Magic Studio Interface](/img/ai-magic-studio/main-interface.png)

## Where to Find It

- **Sidebar:** Click **AI Magic Studio**
- **Direct URL:** `/magic-studio`
- **From projects:** Export to Magic Studio from Create Photoshoot or AI Magic Tools

---

## What is AI Magic Studio?

Think of Magic Studio as your creative workspace where you can:

- **Composite multiple images** into a single scene
- **Apply selective effects** to specific regions using masks
- **Combine AI-generated and uploaded images** seamlessly
- **Fine-tune compositions** with precision tools
- **Export production-ready assets** for ads, social media, and more

### Use Cases

- **Product compositing** - Place products in AI-generated scenes
- **Background replacement** - Swap backgrounds while preserving subjects
- **Creative effects** - Apply effects to specific regions only
- **Ad creative assembly** - Build multi-layer ad compositions
- **Social media graphics** - Combine elements for engaging posts

---

## Interface Overview

The Magic Studio interface consists of:

### Main Canvas

The central workspace where your composition lives:

- **Zoom controls** - Adjust view for detailed work
- **Pan tool** - Navigate large canvases
- **Layer visibility** - Show/hide individual elements
- **Grid & guides** (optional) - Align elements precisely

### Toolbar (Left Side)

Essential tools for creating and editing:

#### Selection & Navigation

- **Pan Tool (H)** - Navigate around the canvas without editing
- **Select Tool (V)** - Select and move layers, resize elements

#### Editing Tools

- **Mask Brush (B)** - Paint masks to define where effects apply
- **Eraser (E)** - Remove parts of layers or masks
- **Remove Background (Q)** - AI-powered background removal

#### Content Tools

- **Add Text (T)** - Insert and style text layers
- **Remove Text (R)** - AI-powered text removal from images
- **Insert Image** - Add new images to your composition
- **Upscale (U)** - AI upscaling for higher resolution

#### History

- **Undo/Redo** - Step backward and forward through changes
- **History panel** - Jump to specific edit states

### Layers Panel (Right Side)

Manage all elements in your composition:

- **Layer order** - Drag to reorder (top layer = front)
- **Visibility toggle** - Show/hide specific layers
- **Lock layers** - Prevent accidental edits
- **Layer opacity** - Adjust transparency
- **Blend modes** - Change how layers interact

### Properties Panel

Adjust settings for the selected tool or layer:

- **Brush size** - For masking and erasing
- **Opacity** - Tool and layer transparency
- **Hardness** - Brush edge softness
- **Effect settings** - Parameters for AI effects

---

## Core Workflows

### 1. Basic Image Compositing

**Combine multiple images into one scene:**

1. **Start with a base** - Upload or import your background image
2. **Add layers** - Click **Insert Image** to add foreground elements
3. **Position elements** - Use **Select Tool (V)** to move and resize
4. **Remove backgrounds** - Select layer, use **Remove Background (Q)**
5. **Blend edges** - Use **Mask Brush** to refine edges
6. **Export** - Download your final composition

**Example:** Place a product photo onto an AI-generated lifestyle scene.

### 2. Selective Effects with Masking

**Apply effects only to specific regions:**

1. **Select your layer** - Click the layer you want to affect
2. **Choose effect** - Apply blur, color grading, or AI effect
3. **Activate Mask Brush (B)** - Paint where the effect should apply
4. **Adjust brush** - Change size and hardness for precision
5. **Refine mask** - Use **Eraser (E)** to remove mask areas
6. **Preview** - Toggle mask visibility to check results

**Example:** Blur just the background while keeping the subject sharp.

### 3. Background Replacement

**Swap backgrounds professionally:**

1. **Import subject image** - Upload photo with subject
2. **Remove background (Q)** - AI removes the original background
3. **Add new background** - Insert desired background as bottom layer
4. **Refine edges** - Use **Mask Brush** to perfect the cutout
5. **Match lighting** - Adjust brightness/color to blend subject
6. **Export** - Save your new composite

**Tip:** After removing background, add a subtle shadow layer beneath your subject for realism.

### 4. Text Integration

**Add styled text to compositions:**

1. **Select Add Text (T)** tool
2. **Click on canvas** - Place your text cursor
3. **Type text** - Enter your message
4. **Style in properties** - Font, size, color, alignment
5. **Position** - Move text layer to desired location
6. **Effects** - Add shadows, outlines, or gradients
7. **Lock layer** - Prevent accidental moves

### 5. Advanced: Multi-Layer Scene Building

**Create complex compositions:**

1. **Plan your layers** - Background, midground, foreground
2. **Import all assets** - Add all images at once
3. **Order layers** - Drag in layers panel (back to front)
4. **Remove backgrounds** - Clean up each element
5. **Apply masks** - Blend elements naturally
6. **Add effects** - Depth blur, color grading, vignettes
7. **Add text/graphics** - Final overlay elements
8. **Export** - Download final composition

---

## Masking Deep Dive

Masking is the most powerful feature in Magic Studio. Mastering it unlocks professional results.

### What is a Mask?

A mask defines **where** an effect or layer is visible:

- **White areas** = Effect applies (100% visible)
- **Black areas** = Effect doesn't apply (0% visible)
- **Gray areas** = Partial effect (50% visible at mid-gray)

### Mask Brush Tips

**For clean edges:**
- Use a **hard brush** (100% hardness)
- Zoom in close (400%+)
- Paint carefully along edges

**For natural blending:**
- Use a **soft brush** (0-30% hardness)
- Lower opacity (50-70%)
- Build up gradually with multiple strokes

**For complex subjects (hair, fur):**
- Use **Remove Background (Q)** first for AI edge detection
- Refine with soft brush at low opacity
- Zoom in to 200-400% for detail work

### Mask Editing Shortcuts

- **B** - Switch to Mask Brush
- **E** - Switch to Eraser (erase mask)
- **[  ]** - Decrease/increase brush size
- **X** - Swap foreground/background color (add/remove)
- **Alt+Click mask** - View mask in isolation

---

## Pro Tips & Techniques

### Workflow Efficiency

1. **Name your layers** - Click layer name to rename (e.g., "Product", "Background", "Shadow")
2. **Use keyboard shortcuts** - Learn H, V, B, E, Q for speed
3. **Group related layers** - Keep compositions organized
4. **Save iterations** - Export versions before major changes
5. **Work non-destructively** - Use masks instead of erasing pixels

### Quality Best Practices

- **Start with high-res images** - You can always downsize, not upsize
- **Match perspective** - Ensure all elements have similar angles
- **Consider lighting** - Match light direction across elements
- **Add shadows** - Grounded subjects look more realistic
- **Color harmony** - Use color grading to unify all elements

### Common Mistakes to Avoid

❌ **Forgetting to remove backgrounds** - Leaves harsh edges  
✅ **Always use Remove Background (Q)** before compositing

❌ **Overlapping without blending** - Looks cut-and-paste  
✅ **Use soft masks** at edges to blend naturally

❌ **Mismatched lighting directions** - Breaks realism  
✅ **Flip/adjust images** to match light sources

❌ **Too many effects** - Composition looks overdone  
✅ **Keep it simple** - Less is often more

---

## Integration with Other Tools

Magic Studio works seamlessly with other CreativioAI features:

### From Create Photoshoot

After generating product images:

1. Select your favorite outputs
2. Click **"Open in Magic Studio"**
3. Automatically loads as layers
4. Combine multiple variations into one hero image

### With AI Magic Tools

Enhance individual elements before compositing:

1. Use **Magic Tools** to upscale, enhance, or remove backgrounds
2. Download enhanced versions
3. Import into **Magic Studio** for composition
4. Build final creative

### Brand Kit Integration

Apply brand consistency:

- Use brand colors for text layers
- Apply brand fonts automatically
- Import brand assets as layers
- Maintain brand guidelines across compositions

---

## Example Workflows

### E-commerce Product Ad

**Goal:** Product on lifestyle background

1. Upload product photo (white background)
2. **Remove Background (Q)** - Extract product cleanly
3. Import AI-generated lifestyle scene as background
4. Position product with **Select (V)**
5. Add drop shadow beneath product (new layer, Gaussian blur)
6. Add text layer with product name and CTA
7. Export 1080x1080 for Instagram

**Time:** ~5 minutes

### Social Media Collage

**Goal:** Multi-image showcase post

1. Create new canvas (1080x1350 for Instagram)
2. Insert 3-4 product images
3. Arrange in grid or creative layout
4. Add colored shape backgrounds
5. Apply brand colors from Brand Kit
6. Add headline text
7. Export for social posting

**Time:** ~8 minutes

### Before/After Comparison

**Goal:** Show transformation clearly

1. Import "before" image
2. Import "after" image
3. Position side-by-side
4. Add vertical dividing line
5. Add "BEFORE" and "AFTER" text labels
6. Export comparison graphic

**Time:** ~3 minutes

---

## Exporting Your Work

### Export Options

- **Format:** PNG (transparent), JPG (smaller file)
- **Resolution:** Original, 2x, 4x (upscaled)
- **Quality:** High, Medium, Low (affects file size)

### Export Settings by Use Case

**Social Media (Instagram, Facebook):**
- Format: JPG
- Resolution: Original or 2x
- Quality: High
- Max dimension: 1080px

**Print/High-Res:**
- Format: PNG
- Resolution: 4x (upscaled)
- Quality: Maximum
- Color profile: CMYK (if available)

**Web/Display Ads:**
- Format: JPG
- Resolution: Original
- Quality: Medium-High
- Optimize for web

**Client Presentation:**
- Format: PNG (for transparency)
- Resolution: 2x
- Quality: High
- Watermark: Optional

---

## Keyboard Shortcuts Reference

| Tool | Shortcut |
|------|----------|
| Pan Tool | H |
| Select Tool | V |
| Mask Brush | B |
| Add Text | T |
| Remove Text | R |
| Eraser | E |
| Remove Background | Q |
| Upscale | U |
| Undo | Ctrl/Cmd + Z |
| Redo | Ctrl/Cmd + Shift + Z |
| Increase Brush Size | ] |
| Decrease Brush Size | [ |
| Zoom In | Ctrl/Cmd + Plus |
| Zoom Out | Ctrl/Cmd + Minus |
| Fit to Screen | Ctrl/Cmd + 0 |

---

## Troubleshooting

### "My edges look jagged"

- Zoom in closer (200-400%) when masking
- Use a softer brush (reduce hardness to 50%)
- Increase brush opacity for smoother coverage
- Use Remove Background (Q) first, then refine

### "Layers aren't blending well"

- Check layer order (drag in layers panel)
- Adjust layer opacity to blend
- Try different blend modes
- Add transition masks at edges

### "Performance is slow"

- Reduce canvas size before starting
- Work with fewer layers
- Merge completed layers (non-destructive copy first)
- Close other browser tabs
- Use lower resolution during editing, upscale at export

### "Can't see my mask"

- Click the mask thumbnail in layers panel
- Look for red overlay showing mask area
- Toggle mask visibility (eye icon)
- Ensure you're painting with white/black

---

## Next Steps

- [Create a photoshoot](/features/create-photoshoot) to generate elements for compositing
- [Use AI Magic Tools](/features/ai-magic-tools) to enhance individual elements
- [Learn workflows](/workflows) for complete creative processes
- [Set up Brand Kit](/features/brand-kit) for branded compositions

## Related Features

- [Create Photoshoot](/features/create-photoshoot) - Generate AI images for compositing
- [AI Magic Tools](/features/ai-magic-tools) - Enhance individual images
- [Animation Studio](/features/animation-studio) - Animate your compositions
- [Brand Kit](/features/brand-kit) - Apply brand assets to compositions
