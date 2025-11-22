# MRT Line Extraction Project

This project experiments with converting schematic MRT maps into structured line data for use in an interactive web visualisation.  
The goal is to extract polylines representing train routes, store their coordinates in JSON, and display them accurately in the browser.

---

## ✅ Purpose

- Convert static MRT diagrams into machine-readable geometry.
- Reduce manual tracing time for large rail networks.
- Prepare data for browser-based mapping with MapLibre.
- Allow future logic, such as route tracing or network analysis.

---

## 🧠 Approach

1. **Pre-processing**
   - Clean the schematic image.
   - Convert to greyscale and threshold to black and white.
   - Resize or deskew if required.

2. **Line Extraction**
   - Detect edges using OpenCV.
   - Apply Hough line transforms to obtain `(ρ, θ)` representations.
   - Filter and merge overlapping or repeated segments.
   - Convert extracted lines into coordinate arrays.

3. **Data Output**
   - Store line coordinates in `mrt_lines.json`.
   - Include metadata such as colour, station sequence, and line name.

4. **Visualisation**
   - Render extracted lines in MapLibre GL JS.
   - Overlay extracted result onto original schematic to verify alignment.

---

