import cv2, json

with open("single_line_points.json") as f:
    data = json.load(f)

pts = data["points"]

canvas = cv2.imread("mrt_clean.png")

for i in range(len(pts)-1):
    p1 = (pts[i]["x"], pts[i]["y"])
    p2 = (pts[i+1]["x"], pts[i+1]["y"])
    cv2.line(canvas, p1, p2, (255,0,0), 5)

cv2.imwrite("rendered_line.png", canvas)
