# -*- coding: utf-8 -*-
"""
Created on Tue Apr  4 10:37:12 2023

@author: alexa
"""

import nazca as nd 



with nd.Cell(name = "Ground external") as Ground_External:
    
    
    for i in range(9):
        
        length = 80
        width = 80
        distance = 300
        nd.strt(length, width, layer = 76).put(0,-i*distance)
        
        
with nd.Cell(name = "Ground connection") as ground_connection:
    for i in range(5):
        
        length = 610
        width = 50
        distance = 600
        nd.strt(length, width, layer = 45).put(0,-i*distance)
    