import cv2
import json
import numpy as np

# -----------------------------------
# Load backdrop image
# -----------------------------------
backdrop = cv2.imread("mrt_clean.png")
if backdrop is None:
    raise RuntimeError("Could not load mrt_clean.png")

canvas = backdrop.copy()

# Ask once for line name
line_id = input("Enter line ID/name: ").strip()
print(f"\n--- Collecting points for line: {line_id} ---")

# Storage for points
points = []

# -----------------------------------
# Mouse callback
# -----------------------------------
def mouse_callback(event, cx, cy, flags, param):
    global points, canvas

    if event == cv2.EVENT_LBUTTONDOWN:
        points.append({"x": int(cx), "y": int(cy)})
        cv2.circle(canvas, (cx, cy), 8, (0, 0, 255), -1)
        print(f"Added point ({cx}, {cy})")


cv2.namedWindow("Point Tool", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Point Tool", 1400, 900)
cv2.setMouseCallback("Point Tool", mouse_callback)

print("\nControls:")
print(" ▸ Left-click to add points")
print(" ▸ Press ENTER to finish and save\n")

# -----------------------------------
# Main loop
# -----------------------------------
while True:
    cv2.imshow("Point Tool", canvas)
    key = cv2.waitKey(1)

    if key == 13:  # ENTER key
        break

cv2.destroyAllWindows()

# -----------------------------------
# Save JSON
# -----------------------------------
output = {
    "line_id": line_id,
    "points": points
}

with open("single_line_points.json", "w") as f:
    json.dump(output, f, indent=4)

print(f"\nSaved to single_line_points.json")
print(f"Total points: {len(points)}")
