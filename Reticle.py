# -*- coding: utf-8 -*-
"""
Created on Fri Sep 23 15:49:16 2022

@author: aliat
"""

import nazca as nd

length=4700
width=2300
cutarea=100
frame_layer=1
def ret(length, width, cutarea,frame_layer):
    l=length
    w=width
    c=cutarea
    assymetric_l = 0
    assymetric_w = 0
    with nd.Cell(name = 'Frame') as myframe:
        nd.Polygon(layer=frame_layer, points = [(0 + assymetric_l ,0 + assymetric_w),(-c,-c),(-c,w+c),(l+c,w+c),(l+c,-c),\
                                                (-c,-c),(0 + assymetric_l ,0 + assymetric_w),(l,0),(l,w),(0,w),(0,0)]).put()
    myframe.put(-l/2,-w/2)


# import nazca as nd

nd.export_gds(filename='Reticle.gds')
            
