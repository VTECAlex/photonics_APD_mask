# -*- coding: utf-8 -*-
"""
Created on Tue May  9 09:48:03 2023

@author: alexa
"""

import nazca as nd 
import nazca.geometries as geom

import doted_circle

# doted_circle.dotted_circle(4,size_of_wafer).put(0,0)


#Ring around the wafer for process 4 

def touch_electrode(layer,size_of_wafer):
    with nd.Cell("Touch electrode for plating") as touch_electrode:
        plating_layer = 4
        size_of_wafer_inches = size_of_wafer
        inche_to_um = 2.54*10000
        sow = inche_to_um*size_of_wafer_inches
        top_bend_offset=6
        top_bend = nd.bend(angle=180-top_bend_offset, radius= 0, width=4000, offset=-sow/2+2000, layer=plating_layer).put(0,0,90+top_bend_offset/2)
        
        
        
        bot_bend_right = nd.bend(angle=75-top_bend_offset, radius= 0, width=4000, offset=-sow/2+2000, layer = plating_layer).put(0,0,+16.775)
        bot_bend_left = nd.bend(angle=75-top_bend_offset, radius= 0, width=4000, offset=-sow/2+2000, layer = plating_layer).put(0,0,-75+top_bend_offset-16.775)
        
        
        
        
        if size_of_wafer == 4:
            nd.strt(length = 22000/2-2500+3800, width = 4000+787.71, layer = plating_layer).put(-22000/2-3800,-36509+2000+30-13117.093+787.71/2+11663.31-11663.337)


            nd.strt(length = 22000/2-2500+3800, width = 4000+787.71, layer = plating_layer).put(2500,-36509+2000+30-13117.093+787.71/2+11663.31-11663.337)
        else:
            nd.strt(length=22000 / 2 - 2500 + 3800, width=4000 + 787.71, layer=plating_layer).put(-22000 / 2 - 3800,
                                                                                                  -36509 + 2000 + 30 - 13117.093 + 787.71 / 2 + 11663.31 )

            nd.strt(length=22000 / 2 - 2500 + 3800, width=4000 + 787.71, layer=plating_layer).put(2500,
                                                                                                  -36509 + 2000 + 30 - 13117.093 + 787.71 / 2 + 11663.31 )
        
        
    return touch_electrode






#nd.bend(angle=180, radius= sow, layer = 5).put(0,0)



# =============================================================================
# 
# nd.strt(length  = 500000 , width = 0.1, layer = 1).put(-100000/2,0)
# nd.strt(width  = 500000 , length = 0.1, layer = 1).put(0,0)
# 
# =============================================================================





nd.export_gds(filename=r'PRclearance')
