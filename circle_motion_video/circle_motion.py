import numpy as np
import cv2

# Create a black image
img = np.zeros((512,512,3), np.uint8)

# Draw a circle
radius = 50
color = (0, 0, 255) # BGR
thickness = -1
center = (256, 256)
cv2.circle(img, center, radius, color, thickness)

# Create a video writer
fourcc = cv2.VideoWriter_fourcc(*"mp4v") # for mp4 format
out = cv2.VideoWriter("circle_movement.mp4", fourcc, 20.0, (512, 512))

# Write the frames to the video
for i in range(60):
    img_copy = img.copy()
    center = (center[0] + 5, center[1] + 5)
    cv2.circle(img_copy, center, radius, color, thickness)
    out.write(img_copy)

# Release the resources
out.release()
cv2.destroyAllWindows()
