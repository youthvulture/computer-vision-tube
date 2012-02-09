#!/usr/bin/env python
# -*- coding: UTF-8 -*-


""" I pieced this script together from the following sources. Mostly to help
help me understand each individual part better, so I can see what's going on.

http://www.betasix.net/opencv-2-2-python-examples/
http://japskua.wordpress.com/2010/08/04/detecting-eyes-with-python-opencv/

Holy buckets, this looks like fun. I look forward to learning more.

TODO: 

Start making cv classes to help me automate some of the high-level business.
"""


import cv
import time
import Image



# Detect the face and eyes of the person in the video screen.
#_____________________________________________________________________________

def detect_face(image):

    # Load face and eye recognition data.
    faceCascade = cv.Load("haarcascade_frontalface_alt.xml")
    eyeCascade = cv.Load("haarcascade_eye.xml")

    # Don't detect any faces smaller than 20x20.
    min_size = (20,20)
    image_scale = 2
    haar_scale = 1.2
    min_neighbors = 2
    haar_flags = 0

    # Generate temporary images for faster processing.
    gray = cv.CreateImage((image.width, image.height), 8, 1)
    small_image = cv.CreateImage((cv.Round(image.width / image_scale), 
                                 cv.Round(image.height / image_scale)), 8 ,1)

    # Convert color input image to grayscale.
    cv.CvtColor(image, gray, cv.CV_BGR2GRAY)

    # Scale input image for faster processing.
    cv.Resize(gray, small_image, cv.CV_INTER_LINEAR)

    # Equalize the histogram.
    cv.EqualizeHist(small_image, small_image)

    # Detect the faces.
    faces = cv.HaarDetectObjects(small_image, faceCascade, 
                                 cv.CreateMemStorage(0), 
                                 haar_scale, 
                                 min_neighbors, 
                                 haar_flags, 
                                 min_size)

    if faces:
        for ((x, y, w, h), n) in faces:
        # the input to cv.HaarDetectObjects was resized, so scale the
        # bounding box of each face and convert it to two CvPoints
            pt1 = (int(x * image_scale), int(y * image_scale))
            pt2 = (int((x + w) * image_scale), int((y + h) * image_scale))
            cv.Rectangle(image, pt1, pt2, cv.RGB(255, 0, 0), 30, 8, 0)
            face_region = cv.GetSubRect(image,(x,int(y + (h/4)),w,int(h/2)))

        cv.SetImageROI(image, (pt1[0],
            pt1[1],
            pt2[0] - pt1[0],
            int((pt2[1] - pt1[1]) * 0.7)))
        eyes = cv.HaarDetectObjects(image, eyeCascade,
        cv.CreateMemStorage(0),
        haar_scale, min_neighbors,
        haar_flags, (15,15))    

        if eyes:
            for eye in eyes:
                cv.Rectangle(image,
                (eye[0][0],
                eye[0][1]),
                (eye[0][0] + eye[0][2],
                eye[0][1] + eye[0][3]),
                cv.RGB(255, 0, 0), 1, 8, 0)

    cv.ResetImageROI(image)
    return image


# 
#_____________________________________________________________________________

def get_webcam_stream(width,height):

    cv.NamedWindow("face_camera", 1)
    capture_webcam = cv.CreateCameraCapture(0)

    # Set the Width and Height of the output screen.
    cv.SetCaptureProperty(capture_webcam, cv.CV_CAP_PROP_FRAME_HEIGHT, height)
    cv.SetCaptureProperty(capture_webcam,cv. CV_CAP_PROP_FRAME_WIDTH, width)

    # Live feed loop.
    while True:
        frame = cv.QueryFrame(capture_webcam)

        # The face detection function is applied here.
        output = detect_face(frame)
        cv.ShowImage("face_camera", output)
        k = cv.WaitKey(10);
        if k == 'f':
            break


# ::: : - - ---        <-*.execute.*.->                          ²¸¹°°­²­¹·³²±
#_____________________________________________________________________________

def main():

    get_webcam_stream(400,300)


if __name__ == "__main__":
    main()
