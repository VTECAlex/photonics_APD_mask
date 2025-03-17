# -*- coding: utf-8 -*-
"""
Created on Wed Oct 12 16:19:13 2022

@author: aliat
"""

import nazca as nd



def stn_cross(iii,jjj):
    
    with nd.Cell(name  = "Cross") as Cross_Stn:
        cross_width = 30
        cross_length  = cross_width*2
        dist = 20
        cross_slayer = 2
        cross_slayer1 = 2
        c_ll = cross_slayer
        c_ll1 = cross_slayer1
        
        
    
        if (iii%2==0 and jjj%2==0) or (iii%2!=0 and jjj%2!=0):
            nd.strt(length = cross_length, width = cross_width, layer = c_ll).put(-cross_length/2,0)
            nd.strt(length = cross_length, width = cross_width, layer = c_ll).put(0,+cross_width,-90)
            
            nd.strt(length = cross_length, width = cross_width, layer = c_ll).put(3*cross_length/2+2*dist,0)
            nd.strt(length = cross_length, width = cross_width, layer = c_ll).put(-(2*(3/2)*cross_length+dist)+10,0)
            
            nd.strt(length = cross_length, width = cross_width, layer = c_ll).put(0,+5*cross_width+2*dist,-90)
            nd.strt(length = cross_length, width = cross_width, layer = c_ll).put(0,-3*cross_width - 2*dist,-90)
        
        
        
        else:
            
            nd.strt(length = cross_length, width = cross_width, layer = c_ll1).put(cross_length/2+dist,0)
            nd.strt(length = cross_length, width = cross_width, layer = c_ll1).put(-((3/2)*cross_length+dist),0)
            
            
            nd.strt(length = cross_length, width = cross_width, layer = c_ll1).put(0,+3*cross_width+dist,-90)
            nd.strt(length = cross_length, width = cross_width, layer = c_ll1).put(0,-cross_width - dist,-90)
            
            nd.strt(length = cross_length, width = cross_width, layer = c_ll1).put(0,+6*cross_width+4.5*dist,-90)
            nd.strt(length = cross_length, width = cross_width, layer = c_ll1).put(0,-4*cross_width - 4.5*dist,-90)
            
            nd.strt(length = cross_length, width = cross_width, layer = c_ll1).put(5*cross_length/2+3*dist,0)
            nd.strt(length = cross_length, width = cross_width, layer = c_ll1).put(-(3*(3/2)*cross_length+dist)+20,0)


    return Cross_Stn.put(-1000,2500)







# =============================================================================
# nd.strt(length = cross_length, width = cross_width, layer = 100).put(0,+cross_width +dist,-90)
#     
# =============================================================================
        
        

        
nd.export_gds(filename='The_Cross.gds')
