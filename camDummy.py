#A dummy camera wrapper (returns only black images and no errors)
import numpy as np

class cam:
    size = (600,400)
    camID = 0
    def __init__(self, _camID):
        self.camID=_camID
        camOpened = True
        if not (camOpened):
            raise ValueError('Failed to open camera')
        
    def setSize(self,_size):
        self.size=_size
        if self.getSize() != _size:
            raise ValueError('Failed to set camera size')
        
    def getSize(self):
        return self.size
        
    def getMaxSize(self):
        return (600,400)

    def getID(self):
        return self.camID
        
    def getFrame(self):
        return np.zeros((self.size[1],self.size[0],3), np.uint8)
        
    def close(self):
        pass
