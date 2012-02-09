#!/usr/bin/env python

import cv


def get_webcam_stream(width,height):

    #cv.NamedWindow("camera", 1)
    capture_webcam = cv.CreateCameraCapture(0)
    while True:
        frame = cv.QueryFrame(capture_webcam)
        cv.ShowImage("camera", frame)

def main():

    get_webcam_stream(100,100)


if __name__ == "__main__":
    main()

