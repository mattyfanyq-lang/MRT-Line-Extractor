import json
import cv2
import numpy as np

# -----------------------------
# Colours (BGR)
# -----------------------------
DTL_COLOUR = (255, 0, 0)      # Blue
EWL_COLOUR = (0, 130, 0)      # Dark green
LINE_THICKNESS = 3

# -----------------------------
# Load JSON (your format)
# -----------------------------
def load_segments(path):
    with open(path, "r") as f:
        data = json.load(f)

    # The uploaded file uses "segments"
    return data["segments"], data["image_width"], data["image_height"]

# -----------------------------
# Draw helper
# -----------------------------
def draw_segments(canvas, segments, colour):
    for seg in segments:
        x1, y1 = seg["x1"], seg["y1"]
        x2, y2 = seg["x2"], seg["y2"]
        cv2.line(canvas, (x1, y1), (x2, y2),
                 colour, LINE_THICKNESS, cv2.LINE_AA)

# -----------------------------
# Main
# -----------------------------
def main():
    # Load both files
    dtl_segs, w, h = load_segments("dtl_v1.json")
    ewl_segs, _, _ = load_segments("ewl_v1.json")  # same size expected

    # White canvas matching image size
    canvas = np.ones((h, w, 3), dtype=np.uint8) * 255

    # Draw each line set
    draw_segments(canvas, dtl_segs, DTL_COLOUR)
    draw_segments(canvas, ewl_segs, EWL_COLOUR)

    # Save output
    cv2.imwrite("combined_lines.png", canvas)
    print("Saved combined_lines.png")

if __name__ == "__main__":
    main()
