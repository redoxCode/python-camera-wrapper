#A wrapper using OpenCV image capture functions
import cv2
import numpy as np

class cam:
    camID = 0
    vc = None
    maxSize=(0,0)
    def __init__(self, _camID):
        self.camID=_camID
        self.vc = cv2.VideoCapture(_camID)
        if not (self.vc.isOpened()):
            raise ValueError('Failed to open camera')
        
        self.maxSize = self.getSize()
        
    def setSize(self,_size):
        self.vc.set(cv2.CAP_PROP_FRAME_WIDTH, _size[0])
        self.vc.set(cv2.CAP_PROP_FRAME_HEIGHT, _size[1])
        #test size:
        if self.getSize() != _size:
            raise ValueError('Failed to set camera size')
        
    def getSize(self):
        _h,_w = self.getFrame().shape[0:2]
        return (_w,_h)
        
    def getMaxSize(self):
        return self.maxSize

    def getID(self):
        return self.camID
        
    def getFrame(self):
        ret,frame = self.vc.read()
        return frame
        
    def close(self):
        self.vc.release()
