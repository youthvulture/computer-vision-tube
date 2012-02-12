#!/usr/bin/env python


import cv



#[:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::]#

class info:

    """This is a class for obtaining various data about a given video sream.
    """

    def __init__(self, input_video):
        self.video = cv.CaptureFromFile(input_video)
        self.width = int(cv.GetCaptureProperty(self.video, 
                                               cv.CV_CAP_PROP_FRAME_WIDTH))
        self.height = int(cv.GetCaptureProperty(self.video, 
                                                cv.CV_CAP_PROP_FRAME_HEIGHT))
        self.fps = int(cv.GetCaptureProperty(self.video, cv.CV_CAP_PROP_FPS))


    #
    #__________________________________________________________________________

    def size(self):
        return (self.width, self.height)


    #
    #__________________________________________________________________________

    def fps(self):
        return self.fps



#[:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::]#

class stream:

    """This is a class for reading and writing videos streams.
    """

    def __init__(self, dimensions, input_video=None):
        self.stream = input_video
        self.height = dimensions[0]
        self.width = dimensions[1]


    # This is a big ugly hack. I need to figure out how to iterate frames.
    #__________________________________________________________________________

    def file(self):
        video = cv.CaptureFromFile(self.stream)
        cv.SetCaptureProperty(video, cv.CV_CAP_PROP_FRAME_HEIGHT, 
                              self.height)
        cv.SetCaptureProperty(video, cv. CV_CAP_PROP_FRAME_WIDTH, 
                              self.width)
        frame_count = int(cv.GetCaptureProperty(video, cv.CV_CAP_PROP_FRAME_COUNT ))

        for i in xrange(frame_count):
            frame = cv.QueryFrame(video)
            cv.ShowImage("video", frame)
            cv.WaitKey(1)


    #
    #__________________________________________________________________________

    def camera(self):
        camera = cv.CreateCameraCapture(0)
        cv.SetCaptureProperty(camera, cv.CV_CAP_PROP_FRAME_HEIGHT, 
                              self.height)
        cv.SetCaptureProperty(camera, cv. CV_CAP_PROP_FRAME_WIDTH, 
                              self.width)
        while True:
            frame = cv.QueryFrame(camera)
            cv.ShowImage("camera", frame)



#[:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::]#

class load:

    def __init__(self):



#[:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::]#

class write:

    def __init__(self):
