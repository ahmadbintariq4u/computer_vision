import cv2 as cv

# video=cv.VideoCapture("video.mp4")
video=cv.VideoCapture(0)
print("Width of the frame: {}".format(video.get(cv.CAP_PROP_FRAME_WIDTH)))
print("Height of the frame: {}".format(video.get(cv.CAP_PROP_FRAME_HEIGHT)))
print("FPS of the frame: {}".format(video.get(cv.CAP_PROP_FPS)))


if video.isOpened() is False:
    print("Error in opening")

frame_index = 0
index=0

while video.isOpened():

    ret, frame = video.read()
    if ret is True:

        cv.imshow('Input frame from the camera', frame)
        # cv.waitKey(1)
        row=200
        col=400
        frame[index:row+index,index:col+index]=0

        cv.imshow('Input frame from the camera', frame)
        cv.waitKey(10)
        index+=1
    
    else:
        break

video.release()
cv.destroyAllWindows()
# cv.waitKey(0)