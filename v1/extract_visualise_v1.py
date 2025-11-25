import sys
import cv2
import numpy as np
import json


# -----------------------------------------------------------
# Improved line detection helper
# -----------------------------------------------------------

def detect_lines(mask):
    kernel = np.ones((3, 3), np.uint8)

    # Morphological close to fill small gaps
    cleaned = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)

    # Opening to remove tiny isolated specks
    cleaned = cv2.morphologyEx(cleaned, cv2.MORPH_OPEN, kernel)

    # More sensitive Hough settings
    lines = cv2.HoughLinesP(
        cleaned,
        rho=1,
        theta=np.pi/180,
        threshold=20,       # Lower threshold for sensitivity
        minLineLength=10,   # Detect very small segments
        maxLineGap=20       # Slightly larger gap allowance
    )

    return lines, cleaned


# -----------------------------------------------------------
# Main extractor with all final fixes
# -----------------------------------------------------------

def main(argv):

    default_file = "mrt_clean.png"
    filename = argv[0] if len(argv) > 0 else default_file

    src = cv2.imread(filename)
    if src is None:
        print("Error: unable to load image.")
        return -1

    height, width = src.shape[:2]

    hsv = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)

    # -------------------------------------------------------
    # Improved purple range:
    #  - includes faint curved purple strokes (lower V/S)
    #  - excludes pink circular icons (H > 160)
    # -------------------------------------------------------
    lower_blue = np.array([100, 80, 40])
    upper_blue = np.array([135, 255, 255])


    # Initial mask
    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    # -------------------------------------------------------
    # FIX 1: Dilation to strengthen curves and reconnect gaps
    # -------------------------------------------------------
    mask = cv2.dilate(mask, np.ones((3, 3), np.uint8), iterations=1)

    # Run detection with improved Hough settings
    lines, cleaned_mask = detect_lines(mask)

    # -------------------------------------------------------
    # Prepare outputs
    # -------------------------------------------------------
    white_canvas = np.ones_like(src) * 255
    overlay = src.copy()

    extracted = {
        "line_name": "Purple",
        "image_width": width,
        "image_height": height,
        "segments": []
    }

    if lines is not None:
        for seg in lines:
            x1, y1, x2, y2 = seg[0]

            # Draw onto white canvas (blue stroke)
            cv2.line(white_canvas, (x1, y1), (x2, y2),
                     (255, 0, 0), 3, cv2.LINE_AA)

            # Draw over original schematic (bright purple)
            cv2.line(overlay, (x1, y1), (x2, y2),
                     (255, 0, 255), 3, cv2.LINE_AA)

            extracted["segments"].append({
                "x1": int(x1), "y1": int(y1),
                "x2": int(x2), "y2": int(y2)
            })

    # -------------------------------------------------------
    # Save everything
    # -------------------------------------------------------
    with open("dtl_v1.1.json", "w") as f:
        json.dump(extracted, f, indent=4)

    cv2.imwrite("dtl_lines_white.png", white_canvas)
    cv2.imwrite("dtl_overlay.png", overlay)
    cv2.imwrite("dtl_mask.png", mask)
    cv2.imwrite("dtl_cleaned_mask.png", cleaned_mask)

    print("Saved files:")

    cv2.imshow("DTL Overlay", overlay)
    cv2.waitKey()

    return 0

if __name__ == "__main__":
    main(sys.argv[1:])
