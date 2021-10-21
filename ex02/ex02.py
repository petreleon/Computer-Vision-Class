import cv2
from os import walk
import re
input_files = "/Users/petreleonardmacamete/code/Computer-Vision-Class/ex02/input"
output_files = "/Users/petreleonardmacamete/code/Computer-Vision-Class/ex02/result"
onlyfiles = [file for file in next(walk(input_files), (None, None, []))[2] if re.match("^.*\.((bmp|BMP|png|PNG|jpg|JPG|tif|TIF))$", file)]
# cv2.imread()
print(onlyfiles)

for file_name in onlyfiles:
    img = cv2.imread(input_files + '/' + file_name)
    height, width = img.shape[:2]
    dim = (width//2, height//2)
    resized = cv2.resize(img, dim)
    cv2.imwrite(output_files + '/' + file_name[:-4] + '_jumatate.jpg', resized)
