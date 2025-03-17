# -*- coding: utf-8 -*-
"""
Created on Thu Sep 22 16:01:04 2022

@author: aliat
"""
###### Custom MMI Alex

import nazca as nd 


def mmi_b(BodyLength, BodyWidth, LegLength, LegWidth, DistEdge , name):
    with nd.Cell(name = 'MMI1x2_{}'.format(name)) as my_mmi:
        layer = 60
        #Design the MMI
        mmi = nd.strt(length = BodyLength , width = BodyWidth , layer = layer ).put(0,0)
        mmi_l1 = nd.strt(length = LegLength, width = LegWidth, layer = layer).put(-LegLength,0)
        mmi_l2 = nd.strt(length = LegLength, width = LegWidth, layer = layer).put(BodyLength, (BodyWidth -LegWidth)/2 -DistEdge)
        mmi_l3 = nd.strt(length = LegLength, width = LegWidth, layer = layer).put(BodyLength, -((BodyWidth -LegWidth)/2 -DistEdge))
        
        #Put pins on the MMI
        nd.Pin('mmi0').put(-LegLength,0,180)
        nd.Pin('mmi1a').put(BodyLength + LegLength, (BodyWidth -LegWidth)/2 -DistEdge ,0)
        nd.Pin('mmi1b').put(BodyLength + LegLength, -((BodyWidth -LegWidth)/2 -DistEdge) ,0)
        
    return my_mmi
            




