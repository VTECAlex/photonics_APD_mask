# -*- coding: utf-8 -*-
"""
Created on Fri Sep 23 15:49:16 2022

@author: aliat
"""

import nazca as nd


def ret(outer_length, outer_width, inner_length,inner_width, frame_layer):
    with nd.Cell(name = 'Reticle Main') as myframe:
        nd.Polygon(layer=frame_layer, points= [(0, 0),
                                               (0, outer_length),
                                               (outer_width, outer_length),
                                               (outer_width, 0),
                                               (0, 0),
                                               ((outer_width-inner_width)/2, (outer_length-inner_length)/2),
                                               ((outer_width-inner_width)/2, (outer_length-inner_length)/2),
                                               ((outer_width - inner_width) / 2 + inner_width,(outer_length - inner_length) / 2),
                                               ((outer_width - inner_width) / 2 + inner_width,(outer_length - inner_length) / 2 + inner_length),
                                               ((outer_width-inner_width)/2, (outer_length-inner_length)/2+inner_length),
                                               ((outer_width - inner_width) / 2, (outer_length - inner_length) / 2),
                                               (0,0)]).put()
    myframe.put(-outer_width/2,-outer_length/2)




#################################
# size_of_wafer = 4
# size_of_reticle = 6
# sow = size_of_wafer
# sor = size_of_reticle
# outer_length = sor * 2.54 * 10000
# outer_width = sor * 2.54 * 10000
# inner_length = sow * 2.54 * 10000
# inner_width = sow * 2.54 * 10000
# ret(outer_length, outer_width, inner_length,inner_width,1)
# nd.export_gds(filename='Reticle_Main.gds')

            
