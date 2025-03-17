# -*- coding: utf-8 -*-
"""
Created on Tue Feb 21 09:13:11 2023

@author: alexa
"""



import nazca as nd
from Invert_text import invert_text
import nazca.geometries as geom
import Reticle
from Invert_text import invert_text


with nd.Cell(name  = "Array_CTLMs") as Array_CTLM:
    outer_ring_r = 142
    gap_distance = 0
    gap_step = 5
    counter_goc = 0
    goc = [8,12,16,20,25,30,35,40,50]
    for j in range(1,4):

        for i in range(1,4):

            with nd.Cell(name = "CTLM{}".format(i)) as CTLM:
                circle_reticle_layer = 2
                middle_circle_r = 50
                cicrle_middle = nd.Polygon(layer=circle_reticle_layer, points=geom.circle(radius=middle_circle_r, N = 700)).put(0,0)
                
                
                gap_distance = gap_distance + gap_step
                inner_ring_r = middle_circle_r+ goc[counter_goc]
                ring_width  = outer_ring_r-inner_ring_r
                ring = nd.Polygon(layer=circle_reticle_layer, points=geom.ring(radius=outer_ring_r , width = ring_width , N = 700)).put(0,0)
                Frame = Reticle.ret( 2*inner_ring_r , 2*inner_ring_r , outer_ring_r-inner_ring_r  , circle_reticle_layer)
                #txt = nd.text("{}um".format(goc[counter_goc]), height=(30), layer=1, box_layer=2, box_buf=20, align="cc")
                counter_goc = counter_goc+1

                #inv = invert_text(txt, 1, 2)
                #inv.put(- outer_ring_r +37.5, outer_ring_r+18)
            CTLM.put((outer_ring_r)*2*i,-(outer_ring_r)*2*j)
            


            
            
            
            
Array_CTLM.put()
nd.export_gds(filename='CTLM_negatives')