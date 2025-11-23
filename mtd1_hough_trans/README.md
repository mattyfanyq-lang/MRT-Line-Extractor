## Comparison of Extraction Methods

### Version 1 — Mask based extraction

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

### Version 2 — Edge based extraction

**Key characteristics**
- Uses Canny edge detection before Hough
- No morphological smoothing, preserving thin boundaries
- Higher Hough threshold and longer minimum line length
- Tuned specifically for the Downtown Line

**Visual result**

✅ Crisp, thin, separated segments  
✅ Cleaner geometry for mapping and JSON output  
❌ May miss very small or faint fragments  


## Visual Samples

### Original MRT Schematic
<div align="center">
  <img src="mrt_clean.png" alt="Original MRT Map" width="500"/>
</div>

---

### Downtown Line Extraction Comparison
<div align="center">

| DTL — Version 1 | DTL — Version 2 |
|-----------------|-----------------|
| <img src="dtl_v1.png" alt="DTL Version 1" width="350"/> | <img src="dtl_v2.png" alt="DTL Version 2" width="350"/> |

</div>

---

### Overlay for DTL - Version 1
<div align="center">
  <img src="dtl_overlay_v1.png" alt="DTL Overlay on Original Map" width="500"/>
</div>

