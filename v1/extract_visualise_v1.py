import sys
import cv2
import numpy as np
import json

def detect_lines(mask):
    kernel = np.ones((3, 3), np.uint8)

    # Morphological close to fill small gaps
    cleaned = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)

    # Opening to remove tiny isolated specks
    cleaned = cv2.morphologyEx(cleaned, cv2.MORPH_OPEN, kernel)

    # Highly sensitive Hough settings
    lines = cv2.HoughLinesP(
        cleaned,
        rho=1,
        theta=np.pi/180,
        threshold=20,       # Lower threshold for sensitivity
        minLineLength=10,   # Detect very small segments
        maxLineGap=20       # Slightly larger gap allowance
    )

    return lines, cleaned

def main(argv):

    default_file = "mrt_clean.png"
    filename = argv[0] if len(argv) > 0 else default_file

    src = cv2.imread(filename)
    if src is None:
        print("Error: unable to load image.")
        return -1

    height, width = src.shape[:2]

    hsv = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)

    lower_green = np.array([45, 60, 40])
    upper_green = np.array([85, 255, 255])


    # Initial mask
    mask = cv2.inRange(hsv, lower_green, upper_green)

    # Dilation to initial mask
    mask = cv2.dilate(mask, np.ones((3, 3), np.uint8), iterations=1)

    # LINE DETECTION
    lines, cleaned_mask = detect_lines(mask)

    # Outputs
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

            # Draw onto white canvas
            cv2.line(white_canvas, (x1, y1), (x2, y2),
                     (0, 130, 0), 3, cv2.LINE_AA)

            # Draw over original schematic
            cv2.line(overlay, (x1, y1), (x2, y2),
                     (255, 0, 255), 3, cv2.LINE_AA)

            extracted["segments"].append({
                "x1": int(x1), "y1": int(y1),
                "x2": int(x2), "y2": int(y2)
            })

    # Save files
    with open("ewl_v1.json", "w") as f:
        json.dump(extracted, f, indent=4)

    cv2.imwrite("ewl_lines_white.png", white_canvas)
    cv2.imwrite("ewl_overlay.png", overlay)
    cv2.imwrite("ewl_mask.png", mask)
    cv2.imwrite("ewl_cleaned_mask.png", cleaned_mask)

    print("Saved files")

    cv2.imshow("EWL Overlay", overlay)
    cv2.waitKey()

    return 0

if __name__ == "__main__":
    main(sys.argv[1:])
