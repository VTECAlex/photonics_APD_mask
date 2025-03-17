# -*- coding: utf-8 -*-
"""
Created on Fri Sep 23 15:18:34 2022

@author: aliat
"""

import nazca as nd
import nazca.demofab as demo
from CustomBend import sbff 

global Au_Plating_Layer, Extra_Mod_Length
Au_Plating_Layer =1
Extra_Mod_Length = 100

def modulator(number, length, width, distance, layer, offset, dcm,ell):
    with nd.Cell(name = 'Modulator(s)') as mymodulator:
        for i in range(0,number//2):
            nd.strt(length = length+ell, width = width, layer = layer).put(-ell/2, distance/2 - distance*dcm*i)
            nd.strt(length = length+ell, width = width, layer = layer).put(-ell/2, - (distance/2+width) -(distance*dcm*i))
            nd.Pin('WavR{}{}'.format(i,'a')).put(length + ell/2,distance/2 - distance*dcm*i)
            nd.Pin('WavR{}{}'.format(i,'b')).put(length +ell/2, - (distance/2+width) - distance*dcm*i)
            nd.Pin('WavL{}{}'.format(i,'a')).put(0-ell/2,distance/2 - distance*dcm*i,180)
            nd.Pin('WavL{}{}'.format(i,'b')).put(0-ell/2,- (distance/2+width) - distance*dcm*i,180)
    return mymodulator

    

def termination_pads(number, length, width, distance, layer, offset, dcm,ell):
    spacing_of_electrodes = 6
    electrode_width = 15 
    electrode_layer = 34
    distance_electrodes = spacing_of_electrodes+electrode_width
    pad_length = 80
    radius_of_top = 100
    electrode_pad_width = 80
    electrode_pad_length = 15
    dist_of_termination_electrodes = 120
    dote = dist_of_termination_electrodes/2+spacing_of_electrodes
    with nd.Cell(name = "Termination Pads") as termination_pad:
        Termination_pads = nd.strt( length = electrode_pad_length , width = electrode_pad_width, layer = Au_Plating_Layer ).put()
        nd.Pin('Temr_Pad_Left').put( electrode_pad_length, electrode_pad_width/2-electrode_width/2 )
        nd.strt(length=80-electrode_pad_length, width = dote, layer = Au_Plating_Layer).put(-(80-electrode_pad_length), -electrode_pad_width/2+dote/2)
    return termination_pad


def TiPtAuelectrodes(number, length, width, distance, layer, offset, dcm,ell):
    with nd.Cell(name = "Electrodes") as TiPtAuelectrodes:
        spacing_of_electrodes = 6
        electrode_width = 15 
        electrode_layer = 34
        Extra_Mod_Length = 100
        
        distance_electrodes = spacing_of_electrodes+electrode_width
        for i in range(0,number//2):
            with nd.Cell(name = "Ti Pt Au Pair of electrodes") as Pair_of_electrodes:
                nd.strt(length = length, width = electrode_width, layer = 8).put(-ell/2,  spacing_of_electrodes/2 - dcm*distance*i)
                nd.strt(length = length, width = electrode_width, layer = 8).put(-ell/2, -(spacing_of_electrodes/2 + electrode_width) -dcm*distance*i )   
            Pair_of_electrodes.put(0, 0 )
            
            
        #################### This is the extra modulation part of TiPtAu
        for i in range(0,number//2):
            with nd.Cell(name = "TiPtAu Extra Mod") as TiPtAu_Extra_Mod:
                nd.strt(length = Extra_Mod_Length, width = 15, layer = 8).put(length+ell/2-Extra_Mod_Length ,  spacing_of_electrodes/2 - dcm*distance*i)
            TiPtAu_Extra_Mod.put(0,0)
        
    return TiPtAuelectrodes


def Au_Plating(number, length, width, distance, layer, offset, dcm, ell, dist_elec_pads, pad_length, where_move):
    with nd.Cell(name = "Au Plating") as Au_Plating:
        spacing_of_electrodes = 6
        electrode_width = 15 
        electrode_layer = 34
        radius_of_top = 100
        for i in range(0,number//2):
            with nd.Cell(name = "Au platin") as Pair_of_electrodes:
                nd.strt(length = length, width = electrode_width, layer = Au_Plating_Layer).put(-ell/2,  spacing_of_electrodes/2 - dcm*distance*i)
                top_bend = nd.bend( radius = radius_of_top , width = electrode_width , angle=-90, layer = Au_Plating_Layer).put()
                termination_pads(number, length, width, distance, layer, offset, dcm, ell).put('Temr_Pad_Left', top_bend.pin['b0'],90)
                #nd.put_stub()
                #termination1.put('Term_Pad_left', top_bend.pin(['a0']))
                nd.strt(length = length, width = electrode_width, layer = Au_Plating_Layer).put(-ell/2, -(spacing_of_electrodes/2 + electrode_width) -dcm*distance*i )
                bot_bend = nd.bend( radius = radius_of_top -spacing_of_electrodes - electrode_width , width = electrode_width , angle=-90, layer = Au_Plating_Layer).put()
                termination_pads(number, length, width, distance, layer, offset, dcm, ell).put('Temr_Pad_Left', bot_bend.pin['b0'], flip = True)
                
                
                ######## The two bends to connect to the Signal and groudn pads
                redius_for_bend_electrodes = 215
                
                
                
                
                first_bend = nd.bend(radius = redius_for_bend_electrodes, angle = 45 , width = electrode_width, layer = Au_Plating_Layer).put('b0', -ell/2, spacing_of_electrodes/2 - dcm*distance*i,180)
                extension_for_extra_modulation_1 = nd.bend(radius = redius_for_bend_electrodes, angle = 45 , width = electrode_width, layer = Au_Plating_Layer).put('a0',first_bend.pin['a0'])
                Connection_Electrodes_Pads(dist_elec_pads, pad_length, where_move, electrode_width).put('Pin_Connection_Electrodes_Pads',extension_for_extra_modulation_1.pin['b0'],flip = True, flop = True)
                
                
                
                
                
                second_bend = nd.bend(radius = redius_for_bend_electrodes, angle = -45 , width = electrode_width, layer = Au_Plating_Layer).put('b0', -ell/2, -(spacing_of_electrodes/2 + electrode_width) - dcm*distance*i,180)
                extension_for_extra_modulation_2 = nd.bend(radius = redius_for_bend_electrodes, angle = -45 , width = electrode_width, layer = Au_Plating_Layer).put('a0',second_bend.pin['a0'])
                Connection_Electrodes_Pads(dist_elec_pads, pad_length, where_move, electrode_width).put('Pin_Connection_Electrodes_Pads',extension_for_extra_modulation_2.pin['b0'], flop = True)
                
                

                
                
                
                
                
                
            Pair_of_electrodes.put()
            
            
# =============================================================================
#             with nd.Cell(name = "Termination for the extra modulation") as Term_for_Extra_modulation:
#                 width_for_extra_mod = 80
#                 length_for_extra_mod = 80
#                 nd.strt(length = length_for_extra_mod, width = width_for_extra_mod, layer = Au_Plating_Layer)
#                 #nd.Pin('Term_Extra_Modul').put()
# =============================================================================
            
            with nd.Cell(name = 'Au plating extra moduladtion ') as Au_plating_extra_modulation:
                width_for_extra_mod = 80
                length_for_extra_mod = 80
                
                
                
                nd.strt(length = Extra_Mod_Length, width = 15, layer = Au_Plating_Layer).put(length+ell/2-Extra_Mod_Length ,  spacing_of_electrodes/2 - dcm*distance*i)
                extension_for_extra_modulation = nd.strt(length = 200, width  = 50, layer = Au_Plating_Layer).put(length+ell/2-Extra_Mod_Length +Extra_Mod_Length/2 , 15 -spacing_of_electrodes +width - dcm*distance*i,90)
                nd.bend(radius = 100, angle = 90, width = 50, layer = Au_Plating_Layer ).put('a0', extension_for_extra_modulation.pin['b0'])
                nd.strt(length = length_for_extra_mod, width = width_for_extra_mod, layer = Au_Plating_Layer).put()
                
                
                
                
            Au_plating_extra_modulation.put()
            
            
            
            
            
    return Au_Plating


def Connection_Electrodes_Pads(dist, pad_length, where_move, electrode_width ):
    
    with nd.Cell(name = 'Connection Electrodes Pads') as Connection_Electrodes_Pads1:
        
        pipes = nd.Polygon(layer= Au_Plating_Layer , points=[(0, electrode_width/2), (0, -electrode_width/2), ( dist , -pad_length/2 +where_move), ( dist , pad_length/2 + where_move  )])
        pipes.put(0,0)
        nd.Pin(name = "Pin_Connection_Electrodes_Pads").put(0,0)
        
        
    #Connection_Electrodes_Pads1.put()
        
    return Connection_Electrodes_Pads1




        


              


nd.export_gds(filename='modulator test file.gds')
