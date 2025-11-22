import json
import cv2
import numpy as np

JSON_FILE = "downtown_line.json"
OUTPUT_IMAGE = "downtown_line_only.png"

def main():
    with open(JSON_FILE, "r") as f:
        data = json.load(f)

    segments = data["segments"]
    img_size = data["image_size"]

    width = img_size["width"]
    height = img_size["height"]

    print(f"Loaded {len(segments)} segments")
    print(f"Canvas size: {width} x {height}")

    img = np.ones((height, width, 3), dtype=np.uint8) * 255

    for seg in segments:
        x1, y1 = seg["x1"], seg["y1"]
        x2, y2 = seg["x2"], seg["y2"]
        cv2.line(img, (x1, y1), (x2, y2), (255, 0, 0), 2)

    cv2.imwrite(OUTPUT_IMAGE, img)
    print(f"Saved DTL-only image to {OUTPUT_IMAGE}")

if __name__ == "__main__":
    main()
