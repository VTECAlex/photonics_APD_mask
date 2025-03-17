# -*- coding: utf-8 -*-
"""
Created on Wed Sep 28 12:17:36 2022

@author: aliat
"""

import nazca as nd
from math import *



nd.add_layer(name = "Waveguide", layer = 2)
nd.add_layer(name = "Test_Layer", layer = 20)


width = 3
SOA_width = 3
length = 50


malakas = nd.Polygon(layer="Waveguide", points=[(0,0), (0, width), (length,SOA_width+abs(SOA_width-width)/2), (length, (SOA_width
                                                                                                              -
                                                                                                              width)/2)]
           )

nd.strt(length = 50, width = 50, layer = 12).put(0,0)
nd.export_gds(filename='TEST.gds')