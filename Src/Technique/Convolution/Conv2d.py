import cv2 as cv
import numpy as np

class Conv2d:
    def __init__(self, inChannel: int, outChannel: int, kernelSize: int):
        # Init the input channel, output channel (feature map) and kernel size
        # Ex inputChannel is RGB -> 3x3. 
        # If number of filtermap is 16 then outChannel is 16
        # The size of filter map expected is 3x3 so kernelSize is 3 too
        
        self.inChannel = inChannel
        self.outChannel = outChannel
        self.kernelSize = kernelSize
        
        self.filters = np.random.randn(out_channels, kernel_size, kernel_size, in_channels) * 0.1
        self.bias = np.random.randn(out_channels) * 0.1