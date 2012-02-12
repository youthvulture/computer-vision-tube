#!/usr/bin/env python
# -*- coding: UTF-8 -*-


"""
201202120259am 

This is an example of how to gather data from various mouse events (in this 
case, (x,y) coordinates), and use this data to control parameters for various
opencv functions.

<-*.JMJ.*->  
"""


import cv



# Define mouse events.
#_____________________________________________________________________________

def onMove(event, x, y, flags, output):
    font = cv.InitFont(cv.CV_FONT_HERSHEY_SIMPLEX, 1.0, 1.0, 0, 1)
    cv.PutText(output, ("%s--%s" % (x,y)), (50,50), font, cv.RGB(x, y, x))
    cv.ShowImage('face_camera', output)
    flags = cv.CV_EVENT_FLAG_LBUTTON


# Generate the viewing window and designate the video source.
#_____________________________________________________________________________

def create_window(name,width,height):
    cv.NamedWindow("face_camera", 1)
    stream = cv.CreateCameraCapture(0)
    cv.SetCaptureProperty(stream, cv.CV_CAP_PROP_FRAME_HEIGHT, height)
    cv.SetCaptureProperty(stream,cv. CV_CAP_PROP_FRAME_WIDTH, width)
    return stream


# Stream the video, already dangit!
#_____________________________________________________________________________

def get_webcam_stream(width,height):


    stream = create_window('face_camera',width,height)
    # Live feed loop.
    while True:
        output = cv.QueryFrame(stream)
        cv.SetMouseCallback("face_camera", onMove, output)
        cv.ShowImage("face_camera", output)


        k = cv.WaitKey(1);
        if k == 'f':
            break


# ::: : - - ---        <-*.execute.*.->                          ²¸¹°°­²­¹·³²±
#_____________________________________________________________________________

def main():

    get_webcam_stream(400,300)

if __name__ == "__main__":
    main()
