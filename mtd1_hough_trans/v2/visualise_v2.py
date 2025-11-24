import json
import cv2
import numpy as np

DTL_FILE = "dtl_v2.json"
EWL_FILE = "ewl_v2.json"
OUTPUT_IMAGE = "combined_dtl_ewl.png"


def load_segments(path):
    with open(path, "r") as f:
        data = json.load(f)
    return data["segments"], data["image_width"], data["image_height"]


def main():

    # ---- Load both files ----
    dtl_segments, dtl_w, dtl_h = load_segments(DTL_FILE)
    ewl_segments, ewl_w, ewl_h = load_segments(EWL_FILE)

    # ---- Ensure same canvas size ----
    width = max(dtl_w, ewl_w)
    height = max(dtl_h, ewl_h)

    print(f"DTL segments: {len(dtl_segments)}")
    print(f"EWL segments: {len(ewl_segments)}")
    print(f"Canvas size: {width} x {height}")

    # ---- Create white canvas ----
    img = np.ones((height, width, 3), dtype=np.uint8) * 255

    # ---- Draw Downtown Line (blue) ----
    for seg in dtl_segments:
        x1, y1 = seg["x1"], seg["y1"]
        x2, y2 = seg["x2"], seg["y2"]
        cv2.line(img, (x1, y1), (x2, y2), (255, 120, 0), 3, cv2.LINE_AA)

    # ---- Draw East–West Line (dark green) ----
    for seg in ewl_segments:
        x1, y1 = seg["x1"], seg["y1"]
        x2, y2 = seg["x2"], seg["y2"]
        cv2.line(img, (x1, y1), (x2, y2), (0, 140, 0), 3, cv2.LINE_AA)

    cv2.imwrite(OUTPUT_IMAGE, img)
    print(f"Saved combined image to {OUTPUT_IMAGE}")


if __name__ == "__main__":
    main()
