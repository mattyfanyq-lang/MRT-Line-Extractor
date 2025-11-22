# MRT Line Extraction Project

This project experiments with converting schematic MRT System Map into structured line data for use in an interactive web visualisation.  
The final goal is to extract polylines representing train routes, store their coordinates in JSON, and render them in the browser.

---

## ✅ Purpose

- Convert static MRT diagrams into machine-readable geometry.
- Prepare data for browser-based mapping with MapLibre.
- Allow future logic implementation

---

## 🧠 Approach

1. **Pre-processing**
   - Clean the schematic image.
   - Convert from .pdf to .png.
   - Convert to greyscale and threshold to black and white.

2. **Line Extraction**
   - Detect edges using OpenCV.
   - Apply Hough line transforms to obtain `(ρ, θ)` representations.
   - Filter and merge overlapping or repeated segments.
   - Convert extracted lines into coordinate arrays.

3. **Data Output**
   - Store line coordinates in `downtown_line.json`.

4. **Visualisation**
   - Overlay extracted result onto original schematic to verify alignment.

---

## 🖼 Visual Samples

Extracting from original schematic:

![Cleaned MRT schematic](mrt_clean.png)

Detected Downtown Line segments:

![Downtown Line only](downtown_line_only.png)

Verification overlay:

![Downtown Line overlay](downtown_overlay.png)

---