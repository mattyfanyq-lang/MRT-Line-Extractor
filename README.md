## Comparison of Extraction Methods

### Version 1 — Mask based extraction

**Key characteristics**

Version 1 starts by masking the target line’s colour, then applies closing, opening, and morphological dilation to smooth gaps and strengthen thin regions. 
The cleaned mask gives the Hough transform a clear and continuous shape to analyse, picking up small angled pieces and faint curves more reliably. 
The result is a dense set of short, accurate (but sometimes overlapping) segments that align closely with the schematic.

**Visual result**

- ✅ Very high sensitivity with strong coverage.
- ✅ Detects many short segments, including faint or curved areas.
- ❌ Generates a large number of line segments, increasing data size and making the output heavier to process.

---

### Version 2 — Edge based extraction

**Key characteristics**

Version 2 runs Canny edge detection instead. 
Canny extracts the thin outline of the Downtown Line, essentially reducing it to a one-pixel path. 
There is no morphological smoothing here, so the structure remains narrow. 
When the Hough transform sees this thinner edge map, it produces fewer but clearer line segments. That gives a much cleaner, more discrete-looking Downtown Line.
Higher Hough thresholds and longer minimum line length used, so shorter fragments get filtered out, strengthening precision.

**Visual result**

- ❌ Fewer segments, reduced coverage
- ❌ Curved sections break down into gaps or disappear entirely
- ✅ Straighter portions look clean, but overall geometry loses fidelity


## Visual Samples

### Colour Masking + Dilation
<div align="center">

| Masked | Masked + Dilation |
|-----------------|-----------------|
| <img src="ewl_mask.png" alt="DTL Version 1" width="500"/> | <img src="ewl_cleaned_mask.png" alt="DTL Version 2" width="500"/> |

</div>

---

### Line Extraction Comparison (DTL + EWL)
<div align="center">

| Version 1 | Version 2 |
|-----------------|-----------------|
| <img src="combined_v1.png" alt="DTL Version 1" width="500"/> | <img src="combined_v2.png" alt="DTL Version 2" width="500"/> |

</div>

---

### Overlay Demo
<div align="center">

| Original MRT System Map | DTL(Version1) overlay |
|-----------------|-----------------|
| <img src="mrt_clean.png" alt="Origanal MRT Schematic" width="500"/> | <img src="dtl_overlay_v1.png" alt="Schematic + DTL(Version1) overlay" width="500"/> |

</div>

---
