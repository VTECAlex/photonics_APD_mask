# -*- coding: utf-8 -*-
"""
Created on Mon Nov 21 16:20:51 2022

@author: aliat
"""

import nazca as nd
##outer
with nd.Cell(name  = "Rulerzz") as Rulerz:
    #outer
    ditance_of_outer = 22000
    lean_width = 10
    bot_ruler_layer = 1
    pitch =50# 35+lean_width/2
    lean_length  = 100
    number_leans = 22000//(2*pitch)
    letter_linewidth = 30
    llw = letter_linewidth
    klm = 0
    for i in range(0,number_leans):
        if i==0:
            
            if klm%2 ==0:
                nd.text("{0:5.0f}".format(i), linewidth = llw).put(200, -llw)
            nd.strt(length =200 , width  = lean_width, layer = 80).put(0,0)

            
        elif i%5==0:
            if klm%2 ==0:
                nd.text("{0:5.0f}".format(-i*pitch), linewidth = llw, layer = bot_ruler_layer).put(200,-pitch*i -llw)
                nd.text("{0:5.0f}".format(i*pitch), linewidth = llw, layer = bot_ruler_layer).put(200,pitch*i -llw)


            nd.strt(length = lean_length , width  = lean_width, layer = bot_ruler_layer).put(0,-pitch*i)
            nd.strt(length = lean_length , width  = lean_width, layer = bot_ruler_layer).put(0,pitch*i)
        else:
            if klm%2 ==0:
                nd.text("{0:5.0f}".format(-i*pitch), linewidth = llw, layer = bot_ruler_layer).put(200,-pitch*i -llw)
                nd.text("{0:5.0f}".format(i*pitch), linewidth = llw, layer = bot_ruler_layer).put(200,pitch*i -llw)


            nd.strt(length = 0.5*lean_length, width  = lean_width, layer = bot_ruler_layer).put(0,-pitch*i)
            nd.strt(length = 0.5*lean_length, width  = lean_width, layer = bot_ruler_layer).put(0,pitch*i)
        klm+=1
 
    nd.text("{0:5.0f}".format(-(i+1)*pitch), linewidth = llw, layer = bot_ruler_layer).put(200,-pitch*(i+1) -llw)
    nd.text("{0:5.0f}".format((i+1)*pitch), linewidth = llw, layer = bot_ruler_layer).put(200,pitch*(i+1) -llw)
    nd.strt(length = 200, width  = lean_width, layer = bot_ruler_layer).put(0,number_leans*pitch)
    
    nd.strt(length = 200, width  = lean_width, layer = bot_ruler_layer).put(0,-number_leans*pitch)