# -*- coding: utf-8 -*-
"""
Created on Fri Sep 23 15:49:16 2022

@author: aliat
"""

import nazca as nd

# =============================================================================
# length=4700
# width=2300
# cutarea=100
# frame_layer=2
# =============================================================================
def frafrafra(length, width, cutarea,frame_layer):
    l=length
    w=width
    c=cutarea
        
    with nd.Cell(name = 'Frame Tile') as myframe:
        nd.Polygon(layer=frame_layer, points = [(0,0),(-c,-c),(-c,w+c),(l+c,w+c),(l+c,-c),\
                                                (-c,-c),(0,0),(l,0),(l,w),(0,w),(0,0)]).put()
    return myframe
                
#nd.export_gds(filename='C:/Users/alexa/Desktop/for work/Wafer design/Frame.gds')
            
