# -*- coding: utf-8 -*-
"""
Created on Tue Apr  4 10:07:48 2023

@author: alexa
"""

import nazca as nd



with nd.Cell(name = "Ground internal") as grounds_internal:
    
    for i in range(5):
        
        length = 200
        width = 200
        distance = 600
        nd.strt(length, width, layer = 34).put(0,-i*distance)