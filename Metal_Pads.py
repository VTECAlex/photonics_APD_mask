# -*- coding: utf-8 -*-
"""
Created on Tue Apr  4 09:23:56 2023

@author: alexa
"""

import nazca as nd 





with nd.Cell(name= "Metal Pads") as metal_pads:
    layer = 100
    length = 80
    width = 80
    distance = 320
    bottom_distnace = 2950
    for i in range(7):
        #top
        nd.strt(length, width , layer=300).put(i*(distance+width),0)
        #bottom
        nd.strt(length, width , layer=300).put(i*(distance+width),-bottom_distnace-width)
#metal_pads.put()
    
#Metal_Pads(2)

#nd.export_gds(filename=r'C:\Users\alexa\Desktop\for work\Klayout Designs GDS files\Modulator Prototype\Metal_Pads')
            