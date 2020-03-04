import json
from watson_developer_cloud import VisualRecognitionV3
import cv2
import os

# connecting to the IBM visual recognition instance, insert version and ibm_key respectively below
visual_recognition = VisualRecognitionV3(
    '2018-03-19',
    iam_apikey=os.environ.get('IBMBETHKEY'))

# uncomment this if you already have a video file

# vidcap = cv2.VideoCapture('output.avi')

# otherwise capture form video cam
cap = cv2.VideoCapture(0)

vidcap = cap

# loop through the video if still recording
while(True):
    # ret, frame = cap.read()
    # # Display the resulting frame
    # cv2.imshow('black and white',frame)
    def getFrame(sec):
        vidcap = cap
        vidcap.set(cv2.CAP_PROP_POS_MSEC,sec*1000)
        hasFrames,image = vidcap.read()
        if hasFrames:
            cv2.imwrite("image"+str(count)+".jpg", image)     # save frame as JPG file
        return hasFrames
    sec = 0
    frameRate = 0.5 #//it will capture image in each 0.5 second
    count=1
    success = getFrame(sec)
    while success:
        count = count + 1
        sec = sec + frameRate
        sec = round(sec, 2)
        success = getFrame(sec)

# go to where the images are being stored
    for filename in os.listdir():
        if filename.endswith(".jpg"): 
            # go through each image created and classify it
            for images in filename:
                with open(filename, 'rb') as images:
                    print(images)
                    classes = visual_recognition.classify(
                    images,
                    threshold='0.6',
                    classifier_ids='tops_1416667987').get_result()
                # print the classified values
                print(json.dumps(classes, indent=2))
            continue
        else:
            continue
    # closing the frame
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()