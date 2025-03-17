# -*- coding: utf-8 -*-
"""
Created on Tue Apr  4 09:57:38 2023

@author: alexa
"""

import nazca as nd


with nd.Cell(name = "Signal Pads") as Signal_Pads:
    
    for i in range(8):
        length = 80
        width = 80
        layer =100
        
        nd.strt(length, width, layer=400).put(0,i*(-300))