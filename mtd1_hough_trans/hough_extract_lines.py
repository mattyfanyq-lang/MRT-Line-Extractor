import cv2
import numpy as np
import json

IMAGE_FILE = "mrt_clean.png"

# ----------------------------
# MRT Line HSV Ranges (tuned)
# ----------------------------

COLOUR_RANGES = {
    "east_west_line": {  # Green
        "lower": (45, 50, 50),
        "upper": (85, 255, 255)
    },
    "north_south_line": {  # Red
        "lower1": (0, 50, 50),
        "upper1": (10, 255, 255),
        "lower2": (170, 50, 50),
        "upper2": (180, 255, 255)
    },
    "circle_line": {  # Yellow / Orange
        "lower": (20, 80, 80),
        "upper": (35, 255, 255)
    },
    "downtown_line": {  # Blue
        "lower": (95, 70, 70),
        "upper": (130, 255, 255)
    },
    "north_east_line": {  # Purple
        "lower": (135, 40, 40),
        "upper": (155, 255, 255)
    },
    "thomson_line": {  # Brown
        "lower": (5, 90, 90),
        "upper": (20, 200, 200)
    }
}

# ----------------------------

def save_segments(name, img, segments):
    h, w = img.shape[:2]

    output = {
        "line": name,
        "image_size": {"width": w, "height": h},
        "segments": segments
    }

    fname = f"{name}.json"
    with open(fname, "w") as f:
        json.dump(output, f, indent=4)

    print(f"Saved {fname} with {len(segments)} segments.")


def detect_lines(mask, img):
    kernel = np.ones((3, 3), np.uint8)
    cleaned = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
    cleaned = cv2.morphologyEx(cleaned, cv2.MORPH_OPEN, kernel)

    # Hough transform
    lines = cv2.HoughLinesP(
        cleaned,
        rho=1,
        theta=np.pi/180,
        threshold=40,
        minLineLength=20,
        maxLineGap=15
    )

    segments = []
    if lines is not None:
        for line in lines:
            x1, y1, x2, y2 = line[0]
            segments.append(
                {"x1": int(x1), "y1": int(y1), "x2": int(x2), "y2": int(y2)}
            )

    return segments


def extract_all():
    img = cv2.imread(IMAGE_FILE)
    if img is None:
        raise FileNotFoundError("Image not found at " + IMAGE_FILE)

    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    for name, ranges in COLOUR_RANGES.items():
        print(f"\nExtracting {name}...")
        
        if name == "north_south_line":
            mask1 = cv2.inRange(hsv, ranges["lower1"], ranges["upper1"])
            mask2 = cv2.inRange(hsv, ranges["lower2"], ranges["upper2"])
            mask = mask1 | mask2
        else:
            mask = cv2.inRange(hsv, ranges["lower"], ranges["upper"])

        segments = detect_lines(mask, img)

        save_segments(name, img, segments)


if __name__ == "__main__":
    extract_all()
