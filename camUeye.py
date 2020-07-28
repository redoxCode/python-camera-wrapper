#A wrapper for IDS Ueye cammeras using pyueye (pip install pyueye)
from pyueye import ueye
import cv2
import numpy as np

class cam:
    camID = 0
    vc = None
    mem_ptr = ueye.c_mem_p()
    mem_id = ueye.int()
    mem_size = (0,0)

    def __init__(self, _camID):
        self.camID=_camID
        self.vc = ueye.HIDS(_camID)
        if not (ueye.is_InitCamera(self.vc, None)==0):
            raise ValueError('Failed to open camera')


        #reserve memory
        self.mem_size = self.getMaxSize()
        ueye.is_AllocImageMem(self.vc, self.mem_size[0], self.mem_size[1],24,self.mem_ptr, self.mem_id)
        
        #set active memory region
        ueye.is_SetImageMem(self.vc, self.mem_ptr, self.mem_id)
 
        #continuous capture to memory
        ueye.is_CaptureVideo(self.vc, ueye.IS_DONT_WAIT)

        
    def setSize(self,_size):
        #TODO
        #test size:
        if self.getSize() != _size:
            raise ValueError('Failed to set camera size')
        
    def getSize(self):
        _h,_w = self.getFrame().shape[0:2]
        return (_w,_h)
        
    def getMaxSize(self):
        sensorinfo = ueye.SENSORINFO()
        ueye.is_GetSensorInfo(self.vc, sensorinfo)
        return (sensorinfo.nMaxWidth.value,sensorinfo.nMaxHeight.value)

    def getID(self):
        return self.camID
        
    def getFrame(self):
        lineinc = self.mem_size[0] * int((24 + 7) / 8)
        frame = ueye.get_data(self.mem_ptr, self.mem_size[0], self.mem_size[1], 24, lineinc, copy=True)
        frame = np.reshape(frame, (self.mem_size[1],self.mem_size[0], 3))
        return frame
                
    def close(self):
        ueye.is_StopLiveVideo(self.vc, ueye.IS_FORCE_VIDEO_STOP)
        ueye.is_ExitCamera(self.vc)
