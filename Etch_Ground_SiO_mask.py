# -*- coding: utf-8 -*-
"""
Created on Tue Apr  4 10:14:18 2023

@author: alexa
"""

import nazca as nd



with nd.Cell(name = "Ground internal") as Etch_Grnd_SiO:
    
    for i in range(5):
        
        length = 210
        width = 210
        distance = 600
        nd.strt(length, width, layer = 99).put(-5,-i*distance)