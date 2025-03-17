# -*- coding: utf-8 -*-
"""
Created on Mon Sep 26 20:27:08 2022

@author: aliat
"""

import nazca as nd 
import nazca.demofab as demo
from math import *





# =============================================================================
# def sbff(offset,width,layer, Bent_name):
#     radius = offset/2
#     with nd.Cell(name  = 'SBent {}'.format(Bent_name)) as SymBent:
#         nd.bend(radius = radius , width = width, layer=layer).put()
#         nd.bend(radius = radius , width = width, angle  = -90, layer=layer).put()
# 
#         nd.Pin('sbentL').put(0,0,180)
#         nd.Pin('sbentR').put(2*radius, 2*radius)
#         nd.put_stub()
# 
#     return SymBent
# =============================================================================


def sbff(offset,width,layer, Bent_name):
    width  = 1.5
    #offset = 4.2
    with nd.Cell(name  = 'SBent {}'.format(Bent_name)) as SymBent:
        
        cb = demo.deep.sbend(width = width, offset= offset).put()
        cb.raise_pins()
    
# =============================================================================
#         nd.Pin('sbentL'.format(Bent_name)).put(0,0,180)
#         nd.Pin('sbentR'.format(Bent_name)).put( dist_mmi_wg , -offset )
# =============================================================================
        #nd.put_stub()
    
        
    return SymBent
