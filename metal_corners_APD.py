# -*- coding: utf-8 -*-
"""
Created on Thu May  4 19:15:28 2023

@author: aliat
"""
import nazca as nd



def Metal_corners(layer):

    with nd.Cell(name  = "Metal Corner") as Metal_Corners:
        nd.strt(length = 200-25, width = 50-25, layer  = layer).put(0,-25/2)
        nd.strt(length = 200-50-25, width = 50, layer  = layer).put(0,-25+50)
        nd.strt(length = 200-50-50-25, width = 50, layer  = layer).put(0,-25+50+50)
        nd.strt(length = 200-50-50-50-25, width = 50, layer  = layer).put(0,-25+50+50+50)


    return Metal_Corners

def Metal_corners_hole(layer):

    with nd.Cell(name="Metal Corner Holes") as Metal_Corners_Holes:
        nd.strt(length=200, width=25, layer=layer).put(0,-25/2)
        nd.strt(length=175, width=50, layer=layer).put(25,25)
        nd.strt(length=125, width=50, layer=layer).put(25+50,25+50)
        nd.strt(length=75, width=50, layer=layer).put(25+50+50,25+50+50)
        nd.strt(length=25, width=25, layer=layer).put(25+50+50+50,50+25+50+50-25/2)
    return Metal_Corners_Holes


# Metal_corners("Centered_AM_Layer",200,2,0,0,0).put()

# nd.export_gds(filename=r'Metal corners')
