import json
import cv2
import numpy as np

JSON_FILE = "downtown_line.json"
BASE_IMAGE = "mrt_clean.png"
OUTPUT_IMAGE = "downtown_overlay.png"

def main():
    with open(JSON_FILE, "r") as f:
        data = json.load(f)

    segments = data["segments"]
    img_size = data["image_size"]

    print(f"Loaded {len(segments)} segments")
    print(f"Image size from JSON: {img_size['width']} x {img_size['height']}")

    img = cv2.imread(BASE_IMAGE)

    if img is None:
        raise FileNotFoundError(f"Could not read base image: {BASE_IMAGE}")

    h, w = img.shape[:2]
    print(f"Actual base image size: {w} x {h}")

    if (w, h) != (img_size["width"], img_size["height"]):
        print("Warning: JSON size and image size differ, "
              "but drawing anyway with JSON coordinates.")

    for seg in segments:
        x1, y1 = seg["x1"], seg["y1"]
        x2, y2 = seg["x2"], seg["y2"]
        cv2.line(img, (x1, y1), (x2, y2), (255, 0, 0), 2)

    cv2.imwrite(OUTPUT_IMAGE, img)
    print(f"Saved overlay to {OUTPUT_IMAGE}")

if __name__ == "__main__":
    main()
