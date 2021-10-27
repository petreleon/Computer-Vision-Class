import cv2
import numpy as np

logo = cv2.imread("ex03/nasa_logo.jpg")
ratio = 0.2
height_logo, width_logo, channels_logo = logo.shape
input_video = cv2.VideoCapture('ex03/ex03.mp4')
fps = input_video.get(cv2.CAP_PROP_FPS)
width_video = int(input_video.get(cv2.CAP_PROP_FRAME_WIDTH))
height_video = int(input_video.get(cv2.CAP_PROP_FRAME_HEIGHT))
max_width_logo = int(width_video*0.2)
max_height_logo_acording_to_max_width_logo = int(height_logo*max_width_logo/width_logo)
max_height_logo = int(height_video*0.2)
max_width_logo_acording_to_max_height_logo = int(width_logo*max_height_logo/height_logo)

if height_logo <= max_height_logo and width_logo <= max_width_logo:
    pass
elif max_height_logo_acording_to_max_width_logo > max_height_logo:
    width_logo = max_width_logo_acording_to_max_height_logo
    height_logo = max_height_logo
    logo = cv2.resize(logo, (width_logo, height_logo))
else:
    width_logo = max_width_logo
    height_logo = max_height_logo_acording_to_max_width_logo
    logo = cv2.resize(logo, (width_logo, height_logo))

fourcc = cv2.VideoWriter_fourcc(*'XVID')
output_movie = cv2.VideoWriter('ex03/videoPrueba.avi', fourcc, fps, (width_video, height_video))
# output_movie = cv2.VideoWriter('videoPrueba.avi', -1, fps, (width_video, height_video))
while True:
    ret, frame = input_video.read()

    if not ret:
        break

    # Following crop assumes the video is colored, 
    # in case it's Grayscale, you may use: crop_img = frame[top:bottom, left:right] 
    # crop_img = frame[top:bottom, left:right, :]
    modified = frame
    modified[:height_logo, -width_logo:] += (ratio * logo).astype(np.dtype('uint8'))
    output_movie.write(modified)


# Closes the video writer.
output_movie.release()
