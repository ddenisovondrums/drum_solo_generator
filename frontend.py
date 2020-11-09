import random 
import numpy as np
import cv2

A4_size = [1754, 1240]
img = np.full((A4_size[0],A4_size[1],3),255, np.uint8)

line_start = [100, 100]
for i in range(1000):
    img[line_start[0], line_start[1] + i] = [165, 165, 165]
    img[line_start[0]+10, line_start[1] + i] = [165, 165, 165]
    img[line_start[0]+20, line_start[1] + i] = [165, 165, 165]
    img[line_start[0]+30, line_start[1] + i] = [165, 165, 165]
    img[line_start[0]+40, line_start[1] + i] = [165, 165, 165]


# for x in range(A4_size[0]):
#     for y in range(A4_size[1]):
#         value = random.randint(0,1)
#         if value == 1:
#             img[x,y] = [0, 0, 0]

# note_coords = [50, 50]

# img[note_coords[0],note_coords[1]] = [0,0,255]

cv2.imwrite("result.png",img)