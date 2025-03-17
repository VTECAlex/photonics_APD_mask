# -*- coding: utf-8 -*-
"""
Created on Fri Sep 30 08:40:58 2022

@author: aliat
"""

import nazca as nd


def ext_con(number, length_ext_con, width, distance_between_them):
    with nd.Cell(name  = 'External Waveguide Connections') as my_external_connections:
        external_cons = {}
        for i in range(0,number):
                
           external_cons['external_cons{}'.format(i)] = nd.strt(length = length_ext_con, width  = width).put(0, -i*distance_between_them)
    return my_external_connections