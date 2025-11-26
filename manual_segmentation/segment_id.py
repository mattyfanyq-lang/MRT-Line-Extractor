import cv2
import json
import numpy as np

# Load backdrop
backdrop = cv2.imread("mrt_clean.png")
if backdrop is None:
    raise RuntimeError("Could not load mrt_clean.png")

H, W = backdrop.shape[:2]

# Storage for the final JSON output
output = {"lines": []}

# Current drawing state
current_points = []
all_segments = []

canvas = backdrop.copy()


# ---------------------------
# Mouse callback
# ---------------------------
def mouse_callback(event, cx, cy, flags, param):
    global current_points, canvas

    if event == cv2.EVENT_LBUTTONDOWN:
        current_points.append({"x": int(cx), "y": int(cy)})
        cv2.circle(canvas, (cx, cy), 8, (0, 0, 255), -1)
        print(f"Added point: ({cx}, {cy})")


cv2.namedWindow("Segmentation Tool", cv2.WINDOW_NORMAL)
cv2.setMouseCallback("Segmentation Tool", mouse_callback)


# ---------------------------
# Main workflow
# ---------------------------

print("Welcome to the manual segmentation tool.")
print("Click to add points.")
print("Press 'S' to finish a segment.")
print("Press ENTER to finish this line.")
print("Press ESC to finish all lines and save JSON.")

while True:

    # Ask for a line name
    line_name = input("\nEnter line name (or blank to finish all work): ").strip()
    if line_name == "":
        break

    all_segments = []
    canvas = backdrop.copy()
    current_points = []

    print(f"\n--- Now segmenting: {line_name} ---")

    while True:
        cv2.imshow("Segmentation Tool", canvas)
        key = cv2.waitKey(1)

        # Finish segment
        if key in [ord('s'), ord('S')]:
            if len(current_points) < 2:
                print("A segment requires at least two clicks.")
                continue

            seg_id = input("Enter segment ID for this segment: ").strip()
            all_segments.append({
                "id": seg_id,
                "points": current_points.copy()
            })

            print(f"Segment '{seg_id}' saved with {len(current_points)} points.")
            current_points = []

        # Finish line
        if key == 13:  # ENTER
            if len(current_points) >= 2:
                seg_id = input("Enter segment ID for last unfinished segment: ").strip()
                all_segments.append({
                    "id": seg_id,
                    "points": current_points.copy()
                })
                print(f"Segment '{seg_id}' saved.")

            break

        # Finish everything
        if key == 27:  # ESC
            break

    # Store the line
    output["lines"].append({
        "line_name": line_name,
        "segments": all_segments
    })

    if key == 27:
        break

cv2.destroyAllWindows()


# ---------------------------
# Save JSON
# ---------------------------
with open("manual_lines.json", "w") as f:
    json.dump(output, f, indent=4)

print("\nSaved → manual_lines.json")
print("All done.")
