## Comparison of Extraction Methods

### Version 1 — Mask based extraction

**Key characteristics**

Version 1 takes the raw colour mask and applies morphological closing and opening. 
This expands the blue Downtown Line, fills tiny gaps, and reconnects broken parts. 
The line becomes thicker in pixel terms, so the Hough transform receives a large, continuous region of blue pixels. 
As a result, it detects many similar line segments stacked on top of one another, which makes the output look clustered and visually busy.
Lower Hough thresholds and shorter minimum line lengths are used, which encourages extra detections.

**Visual result**

✅ High sensitivity  
✅ Captures many short segments  
❌ Produces dense, clustered and overlapping lines  

---

### Version 2 — Edge based extraction

**Key characteristics**

Version 2 runs Canny edge detection instead. 
Canny extracts the thin outline of the Downtown Line, essentially reducing it to a one-pixel path. 
There is no morphological smoothing here, so the structure remains narrow. 
When the Hough transform sees this thinner edge map, it produces fewer but clearer line segments. That gives a much cleaner, more discrete-looking Downtown Line.
Higher Hough thresholds and longer minimum line length used, so shorter fragments get filtered out, strengthening precision.

**Visual result**

✅ Crisp, thin, separated segments  
✅ Cleaner geometry for mapping and JSON output  
❌ May miss very small or faint fragments  


## Visual Samples

### Downtown Line Extraction Comparison
<div align="center">

| DTL — Version 1 | DTL — Version 2 |
|-----------------|-----------------|
| <img src="dtl_v1.png" alt="DTL Version 1" width="500"/> | <img src="dtl_v2.png" alt="DTL Version 2" width="500"/> |

</div>

---

### Overlay Demo
<div align="center">

| Origanal MRT Schematic | Schematic + DTL(Version1) overlay|
|-----------------|-----------------|
| <img src="mrt_clean.png" alt="Origanal MRT Schematic" width="500"/> | <img src="dtl_overlay_v1.png" alt="Schematic + DTL(Version1) overlay" width="500"/> |

</div>

---

### DTL + EWL Combined Line Visualisation — Version 2
<div align="center">
  <img src="combined_dtl_ewl.png" alt="Visualisation for EWL and DTLp" width="600"/>
</div>

