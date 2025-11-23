## Comparison of Extraction Methods

### Method 1 — Morph + Hough

**Key characteristics**
- Works on the raw HSV colour mask
- Uses morphological closing and opening to smooth regions
- Lower Hough thresholds and shorter minimum line length
- Designed for extracting multiple MRT lines in one pass

**Visual result**
✅ High sensitivity  
✅ Captures many short segments  
❌ Produces dense, clustered and overlapping lines  

---

### Method 2 — Optimised for Hough only

**Key characteristics**
- Uses Canny edge detection before Hough
- No morphological smoothing, preserving thin boundaries
- Higher Hough threshold and longer minimum line length
- Tuned specifically for the Downtown Line

**Visual result**
✅ Crisp, thin, separated segments  
✅ Cleaner geometry for mapping and JSON output  
❌ May miss very small or faint fragments  


## 🖼 Visual Samples

Extracting from original schematic:

![Cleaned MRT schematic](mrt_clean.png)

Detected Downtown Line segments:

![Downtown Line only](downtown_line_only.png)

Verification overlay:

![Downtown Line overlay](downtown_overlay.png)

---