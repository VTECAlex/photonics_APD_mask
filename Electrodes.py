# -*- coding: utf-8 -*-
"""
Created on Fri Sep 23 15:18:34 2022

@author: aliat
"""

import nazca as nd
import nazca.demofab as demo
from CustomBend import sbff 



def modulator(number, length, width, distance, layer, offset, dcm):
        
    with nd.Cell(name = 'Modulator(s)') as mymodulator:
        for i in range(0,number//2):
            nd.strt(length = length, width = width, layer = layer).put(0, 0 - distance*dcm*i)
            nd.strt(length = length, width = width, layer = layer).put(0, - (distance + distance*dcm*i))
            
            nd.Pin('WavR{}{}'.format(i,'a')).put(length,0 - distance*dcm*i)
            nd.Pin('WavR{}{}'.format(i,'b')).put(length, - distance - distance*dcm*i)
            nd.Pin('WavL{}{}'.format(i,'a')).put(0,0 - distance*dcm*i,180)
            nd.Pin('WavL{}{}'.format(i,'b')).put(0,- distance - distance*dcm*i,180)
    return mymodulator


# =============================================================================
# number = 10
# length = 2000
# width = 2
# distance = 300
# layer = 2
# offset = distance/2
# =============================================================================
# =============================================================================
# modulator1 = modulator(number, length, width, distance, layer, offset).put()
# 
# b = {}
# for i in range(0,number//2):
#     b['sbentL{}a'.format(i)] = sbff(offset, width, layer).put(modulator1.pin['WavL{}a'.format(i)])
#     b['sbentL{}b'.format(i)] = sbff(offset, width, layer).put(modulator1.pin['WavL{}b'.format(i)],flip = True)
#     
#     b['sbentR{}a'.format(i)] = sbff(offset, width, layer).put(modulator1.pin['WavR{}a'.format(i)], flip = True)
#     b['sbentR{}b'.format(i)] = sbff(offset, width, layer).put(modulator1.pin['WavR{}b'.format(i)])
# =============================================================================
    
    
    


              


#nd.export_gds(filename='C:/Users/aliat/OneDrive/Desktop/for work/Klayout Designs GDS files/modulator test file.gds')
