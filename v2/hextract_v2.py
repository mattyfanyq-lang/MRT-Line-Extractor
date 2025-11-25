import sys
import cv2 as cv
import numpy as np
import json


def main(argv):

    default_file = "mrt_clean.png"
    filename = argv[0] if len(argv) > 0 else default_file

    src = cv.imread(cv.samples.findFile(filename))
    if src is None:
        print("Error opening image!")
        print("Usage: extract_downtown_line.py [image_name -- default " + default_file + "]\n")
        return -1

    height, width = src.shape[:2]

    hsv = cv.cvtColor(src, cv.COLOR_BGR2HSV)

    lower_green = np.array([50, 120, 120])
    upper_green = np.array([80, 255, 255])

    mask = cv.inRange(hsv, lower_green, upper_green)
    edges = cv.Canny(mask, 50, 200, None, 3)

    result = np.copy(src)

    linesP = cv.HoughLinesP(
        edges,
        1,
        np.pi / 180,
        threshold=50,
        minLineLength=60,
        maxLineGap=15
    )
    extracted = {
        "line_name": "Downtown Line",
        "image_width": width,
        "image_height": height,
        "segments": []
    }

    if linesP is not None:
        for seg in linesP:
            x1, y1, x2, y2 = seg[0]
            cv.line(result, (x1, y1), (x2, y2), (255, 0, 0), 3, cv.LINE_AA)
            extracted["segments"].append({
                "x1": int(x1),
                "y1": int(y1),
                "x2": int(x2),
                "y2": int(y2)
            })

    with open("ewl_v2.json", "w") as f:
        json.dump(extracted, f, indent=4)

    print("Saved extracted segments and image size to downtown_line.json")

    cv.imshow("Extracted Line", result)
    cv.waitKey()
    return 0


if __name__ == "__main__":
    main(sys.argv[1:])
