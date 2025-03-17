# -*- coding: utf-8 -*-
"""
Created on Fri Dec  2 14:37:55 2022

@author: aliat
"""

import nazca as nd 
import nazca.geometries as geom


with nd.Cell("CTLM_1") as CTLM_trololo:
    
    ctlm_layer = 2
    inner_circle_radius = 30
    pitch_of_outer_rings = 200
    width_of_the_rings = 30
    
    icr = inner_circle_radius
    poor = pitch_of_outer_rings
    wotr = width_of_the_rings
    
    nd.text("D:60um,460um,860um,1260um",layer= ctlm_layer).put(-300,700)
    
    nd.Polygon(layer = ctlm_layer, points=geom.circle(icr, N=100)).put(0,0)
    nd.Polygon(layer = ctlm_layer, points=geom.ring(icr+poor, width = wotr, N=100)).put(0,0)
    nd.Polygon(layer = ctlm_layer, points=geom.ring(icr+2*poor, width = wotr, N=100)).put(0,0)
    nd.Polygon(layer = ctlm_layer, points=geom.ring(icr+3*poor, width = wotr, N=100)).put(0,0)




# =============================================================================
# def CTLM_sup():
#     CTLM.put(0,0)
# =============================================================================
CTLM_trololo.put(0,0)  
nd.export_gds(filename='CTLMS.gds')