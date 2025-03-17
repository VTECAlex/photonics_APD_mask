# -*- coding: utf-8 -*-
"""
Created on Mon Oct 10 08:57:31 2022
CREATE LETTERS
@author: aliat
"""



import nazca as nd
from math import *
import nazca.geometries as geom


def dotted_circle(layer,size_of_wafer):
    with nd.Cell(name  = "Dotted_Circle") as DottedCircle:
        dot_length = 30
        dot_width = 50
        # size_of_wafer = size_of_wafer
        sow = size_of_wafer*2.54
        
        #print(layer)
        if layer in [1,2,3]:
            radius  = sow*10000/2 #76.2
        else:
            radius  = sow*10000/2 +30
            
            
        #print(radius)
        number_points = 3000
        x = 0
        R = radius-dot_length
        dotted_cicrcle_layer = layer
     
        tt = 0
        major_flat_length = 32.5*1000
        if size_of_wafer == 3:
            major_flat_length =  22 * 1000

        minor_flat_length = 0 #11*1000
        
        l = major_flat_length
        ll = minor_flat_length
        
        phi = (asin((l/2)/R))
        phiphi = (asin((ll/2)/R))
        
        theta = (pi-2*phi)/2
        step = 2*pi/(number_points)
        

    
        for i in range(0,number_points+1):
            if tt>phiphi and tt<pi+theta or tt>2*pi-theta and tt<2*pi-phiphi:
                #print(tt)
                nd.strt(length  = dot_length, width = dot_width, layer = dotted_cicrcle_layer).put((R)*cos(tt), (R)*sin(tt),180*tt/pi)
            tt = tt + step
            
        #For the Major Flat
        for i in range(0,int((l//dot_width)//2)+1):
            step = l /((l/dot_width))
            xxx = dot_width/(int((l//dot_width)//2))
            nd.strt(length = dot_width, width = dot_length, layer = dotted_cicrcle_layer).put(-R*cos(theta)+i*(step+dot_width-xxx), -R*sin(theta)-dot_length/2 - 1.335)
            
        #for the minor flat
        for i in range(0,int((ll//dot_width)//2)):
            step = ll /(ll/dot_width)
            nd.strt(length = dot_length, width = dot_width, layer = dotted_cicrcle_layer).put(sqrt(R**2-(ll/2)**2)-dot_length, -ll/2+dot_width/2 +i*(step+dot_width)) #put(sqrt(R**2-(ll/2)**2), -ll/2+step+dot_length/2)

    return DottedCircle

# dotted_circle(4,size_of_wafer).put(0,0)
# dotted_circle(2,size_of_wafer).put(0,0)








# nd.export_gds(filename=r'C:\Users\alexa\Desktop\APD designs\DottedCircle.gds')
