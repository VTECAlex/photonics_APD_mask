# -*- coding: utf-8 -*-
"""
Created on Thu Oct  6 16:32:40 2022
LEAN DESIGN
@author: aliat
"""

import nazca as nd
##outer
with nd.Cell(name  = "half_lean") as leanSSS:
    #outer
    ditance_of_outer = 2100
    lean_width = 10

    pitch =50# 35+lean_width/2
    lean_length  = 100
    number_leans = 25
    letter_linewidth = 30
    llw = letter_linewidth
    klm = 0
    layer_lean = 1
    for i in range(0,number_leans):
        if i==0:
            nd.strt(length =200 , width  = lean_width, layer = 2).put(0,0)
        elif i%5==0:
            if klm%5 ==0:
                nd.text("{0:5.0f}".format(-i*pitch), linewidth = llw, layer = layer_lean).put(200,-pitch*i -llw)
                nd.text("{0:5.0f}".format(i*pitch), linewidth = llw, layer = layer_lean).put(200,pitch*i -llw)
            nd.strt(length = lean_length , width  = lean_width, layer = layer_lean).put(0,-pitch*i)
            nd.strt(length = lean_length , width  = lean_width, layer = layer_lean).put(0,pitch*i)
        else:
            if klm%5 ==0:
                nd.text("{0:5.0f}".format(-i*pitch), linewidth = llw, layer = layer_lean).put(200,-pitch*i -llw)
                nd.text("{0:5.0f}".format(i*pitch), linewidth = llw, layer = layer_lean).put(200,pitch*i -llw)


            nd.strt(length = 0.5*lean_length, width  = lean_width, layer = layer_lean).put(0,-pitch*i)
            nd.strt(length = 0.5*lean_length, width  = lean_width, layer = layer_lean).put(0,pitch*i)
        klm+=1
 
    nd.text("{0:5.0f}".format(-(i+1)*pitch), linewidth = llw, layer = layer_lean).put(200,-pitch*(i+1) -llw)
    nd.text("{0:5.0f}".format((i+1)*pitch), linewidth = llw, layer = layer_lean).put(200,pitch*(i+1) -llw)
    nd.strt(length = 200, width  = lean_width, layer = layer_lean).put(0,number_leans*pitch)
    
    nd.strt(length = 200, width  = lean_width, layer = layer_lean).put(0,-number_leans*pitch)

leanSSS.put()
            
            
            
nd.export_gds(filename='Lean_half.gds')

