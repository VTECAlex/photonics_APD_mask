# -*- coding: utf-8 -*-
"""
Created on Wed Sep 28 09:32:34 2022

@author: aliat
"""

import nazca as nd
from MZmodulator import *
from CustomBend import sbff 
from mmi1x2 import mmi_b as mmi





########################################### remove after########################
#from ModulationArea import Modulation
from external_connections import ext_con
from math import *
from nazca.interconnects import Interconnect
################################################################################





def Modulation(number, length, width, distance, layer, BodyLength, BodyWidth, LegLength, LegWidth, DistEdge, dcm,dist_mmi_wg,ell , dist_elec_pads, pad_length, where_move):
    with nd.Cell(name = 'ModulationArea') as ModulationArea:
    
        offset = distance/2 +width - BodyWidth/2+DistEdge
        modulator1 = modulator(number, length, width, distance, layer, offset,dcm,ell).put(0,width/2)
        
        electrode_width = 15
        
        TiPtAuelectrodes(number, length, width, distance, layer, offset, dcm,ell).put(0, electrode_width/2)
        Au_Plating(number, length, width, distance, layer, offset, dcm,ell, dist_elec_pads, pad_length, where_move ).put(0, electrode_width/2)
        d = {}
        d1 = {}
        d2 = {}

        for i in range(0,number//2): #####PUTS THE BENTS ON THE SPECIFIED PINS OF THE MODULATOR
            d1[i] = sbff(offset, width, layer, "L{}a".format(i)).put(modulator1.pin['WavL{}b'.format(i)], flip = True)
            sbff(offset, width, layer, "L{}b".format(i)).put(modulator1.pin['WavL{}a'.format(i)])
            
            
            d2[i] = sbff(offset, width, layer, "R{}a".format(i)).put(modulator1.pin['WavR{}b'.format(i)])
            sbff(offset, width, layer, "R{}b".format(i)).put('a0', modulator1.pin['WavR{}a'.format(i)], flip = True )
            
            d['mmiL{}'.format(i)] = mmi(BodyLength, BodyWidth, LegLength, LegWidth, DistEdge, 'L{}'.format(i)).put('mmi1a',d2[i].pin['b0'])
            d['mmiL{}'.format(i)].raise_pins(['mmi0'],['mmi0L{}'.format(i)])
            
            d['mmiR{}'.format(i)] = mmi(BodyLength, BodyWidth, LegLength, LegWidth, DistEdge, 'R{}'.format(i)).put('mmi1b', d1[i].pin['b0'])
            d['mmiR{}'.format(i)].raise_pins(['mmi0'],['mmi0R{}'.format(i)])


    return ModulationArea




nd.export_gds(filename=r'Modulation_Area')