# -*- coding: utf-8 -*-
"""
Created on Tue Apr  4 09:13:15 2023

@author: alexa
"""

import nazca as nd
import Modulator_Full_Design
import Frame_for_tile
import Metal_Pads
import Signal_Pads
import Ground_Internal
import Etch_Ground_SiO_mask
import Ground_External
from MZmodulator import *
import nazca.geometries as geom
import Reticle
import Dark_Current_PCM_V3
import Device_Tile_V2
from Invert_text import invert_text
import metal_corners
from collections import defaultdict
import Dark_Current_PCM

import Tile

def Tile_PCMs_all(extra_length, Quadrant, i,j):
    


    row_ID = j+1
    column_ID = i +1
    nd.add_layer(name='MESA etch', layer=1, accuracy=0.001)
    nd.add_layer(name='Planar Ring', layer=222, accuracy=0.001)

    nd.add_layer(name='SiO', layer=2, accuracy=0.001)
    nd.add_layer(name='Metal Rings', layer=3, accuracy=0.001)
    nd.add_layer(name='Metal Ring Openings', layer=33, accuracy=0.001)
    nd.add_layer(name='N Metal', layer=5, accuracy=0.001)
    nd.add_layer(name='Au plating ', layer=6, accuracy=0.001)
    nd.add_layer(name='Open Corners', layer=23, accuracy=0.001)
    nd.add_layer(name='lay22', layer=22, accuracy=0.001)  # this is the layer to remove for the N-type contacts later
    metal_pads_layer = 50
    x_move = +300-7.5-151.25
    y_move = -1150-700
    with nd.Cell(name = 'One tile') as Single_Tile:
        ######## All fixed here don't change ##############
        frame_length = 3600+3100
        frame_width = 4900
        fram_cut_area = 100

        Frame_for_tile.frafrafra(frame_length + extra_length , frame_width, fram_cut_area, 1).put(-frame_length/2 -extra_length/2 +3000/2+50 , -frame_width/2)
        Frame_for_tile.frafrafra(frame_length + extra_length , frame_width, fram_cut_area, 2).put(-frame_length/2 -extra_length/2 +3000/2+50, -frame_width/2)

        width_wvg = 1.5
        text_position_x = -extra_length/2-1345+200-120-500+500+1350
        text_position_y =1328.625
        text_position_y_layer_ID = -745+300+300-700-1500-145+4
        text_rotation = -90
        text_height = 200
        
        
        
        
        
        with nd.Cell(name  = "Cross") as Left_Cross_Stn:
            cross_width = 30
            cross_length  = cross_width*2
            dist = 20
            cross_slayer = 'Planar Ring'
            cross_slayer1 = 'SiO'
            c_ll = cross_slayer
            c_ll1 = cross_slayer1
            
            
            #Half part
            nd.strt(length = cross_length, width = cross_width, layer = c_ll).put(-cross_length/2,0)
            nd.strt(length = cross_length, width = cross_width, layer = c_ll).put(0,+cross_width,-90)
            
            nd.strt(length = cross_length, width = cross_width, layer = c_ll).put(3*cross_length/2+2*dist,0)
            nd.strt(length = cross_length, width = cross_width, layer = c_ll).put(-(2*(3/2)*cross_length+dist)+10,0)
            
            nd.strt(length = cross_length, width = cross_width, layer = c_ll).put(0,+5*cross_width+2*dist,-90)
            nd.strt(length = cross_length, width = cross_width, layer = c_ll).put(0,-3*cross_width - 2*dist,-90)
            #The other half part
            
            nd.strt(length = cross_length, width = cross_width, layer = c_ll1).put(cross_length/2+dist,0)
            nd.strt(length = cross_length, width = cross_width, layer = c_ll1).put(-((3/2)*cross_length+dist),0)
            
            
            nd.strt(length = cross_length, width = cross_width, layer = c_ll1).put(0,+3*cross_width+dist,-90)
            nd.strt(length = cross_length, width = cross_width, layer = c_ll1).put(0,-cross_width - dist,-90)
            
            nd.strt(length = cross_length, width = cross_width, layer = c_ll1).put(0,+6*cross_width+4.5*dist,-90)
            nd.strt(length = cross_length, width = cross_width, layer = c_ll1).put(0,-4*cross_width - 4.5*dist,-90)
            
            nd.strt(length = cross_length, width = cross_width, layer = c_ll1).put(5*cross_length/2+3*dist,0)
            nd.strt(length = cross_length, width = cross_width, layer = c_ll1).put(-(3*(3/2)*cross_length+dist)+20,0)
        with nd.Cell(name  = "Cross") as Mid_Cross_Stn:
            cross_width = 30
            cross_length  = cross_width*2
            dist = 20
            cross_slayer = 'SiO'
            cross_slayer1 = 'Metal Rings'
            c_ll = cross_slayer
            c_ll1 = cross_slayer1
            
            
            #Half part
            nd.strt(length = cross_length, width = cross_width, layer = c_ll).put(-cross_length/2,0)
            nd.strt(length = cross_length, width = cross_width, layer = c_ll).put(0,+cross_width,-90)
            
            nd.strt(length = cross_length, width = cross_width, layer = c_ll).put(3*cross_length/2+2*dist,0)
            nd.strt(length = cross_length, width = cross_width, layer = c_ll).put(-(2*(3/2)*cross_length+dist)+10,0)
            
            nd.strt(length = cross_length, width = cross_width, layer = c_ll).put(0,+5*cross_width+2*dist,-90)
            nd.strt(length = cross_length, width = cross_width, layer = c_ll).put(0,-3*cross_width - 2*dist,-90)
            #The other half part
            
            nd.strt(length = cross_length, width = cross_width, layer = c_ll1).put(cross_length/2+dist,0)
            nd.strt(length = cross_length, width = cross_width, layer = c_ll1).put(-((3/2)*cross_length+dist),0)
            
            
            nd.strt(length = cross_length, width = cross_width, layer = c_ll1).put(0,+3*cross_width+dist,-90)
            nd.strt(length = cross_length, width = cross_width, layer = c_ll1).put(0,-cross_width - dist,-90)
            
            nd.strt(length = cross_length, width = cross_width, layer = c_ll1).put(0,+6*cross_width+4.5*dist,-90)
            nd.strt(length = cross_length, width = cross_width, layer = c_ll1).put(0,-4*cross_width - 4.5*dist,-90)
            
            nd.strt(length = cross_length, width = cross_width, layer = c_ll1).put(5*cross_length/2+3*dist,0)
            nd.strt(length = cross_length, width = cross_width, layer = c_ll1).put(-(3*(3/2)*cross_length+dist)+20,0)
        with nd.Cell(name  = "Cross") as Right_Cross_Stn:
            cross_width = 30
            cross_length  = cross_width*2
            dist = 20
            cross_slayer = 'Metal Rings'
            cross_slayer1 = 'N Metal'
            c_ll = cross_slayer
            c_ll1 = cross_slayer1
            
            
            #Half part
            nd.strt(length = cross_length, width = cross_width, layer = c_ll).put(-cross_length/2,0)
            nd.strt(length = cross_length, width = cross_width, layer = c_ll).put(0,+cross_width,-90)
            
            nd.strt(length = cross_length, width = cross_width, layer = c_ll).put(3*cross_length/2+2*dist,0)
            nd.strt(length = cross_length, width = cross_width, layer = c_ll).put(-(2*(3/2)*cross_length+dist)+10,0)
            
            nd.strt(length = cross_length, width = cross_width, layer = c_ll).put(0,+5*cross_width+2*dist,-90)
            nd.strt(length = cross_length, width = cross_width, layer = c_ll).put(0,-3*cross_width - 2*dist,-90)
            #The other half part
            
            nd.strt(length = cross_length, width = cross_width, layer = c_ll1).put(cross_length/2+dist,0)
            nd.strt(length = cross_length, width = cross_width, layer = c_ll1).put(-((3/2)*cross_length+dist),0)
            
            
            nd.strt(length = cross_length, width = cross_width, layer = c_ll1).put(0,+3*cross_width+dist,-90)
            nd.strt(length = cross_length, width = cross_width, layer = c_ll1).put(0,-cross_width - dist,-90)
            
            nd.strt(length = cross_length, width = cross_width, layer = c_ll1).put(0,+6*cross_width+4.5*dist,-90)
            nd.strt(length = cross_length, width = cross_width, layer = c_ll1).put(0,-4*cross_width - 4.5*dist,-90)
            
            nd.strt(length = cross_length, width = cross_width, layer = c_ll1).put(5*cross_length/2+3*dist,0)
            nd.strt(length = cross_length, width = cross_width, layer = c_ll1).put(-(3*(3/2)*cross_length+dist)+20,0)

            ###############
            with nd.Cell(name="Cross") as Extra_Right_Cross_Stn:
                cross_width = 30
                cross_length = cross_width * 2
                dist = 20
                cross_slayer = 'Metal Rings'
                cross_slayer1 = 'Au plating '
                c_ll = cross_slayer
                c_ll1 = cross_slayer1

                # Half part
                nd.strt(length=cross_length, width=cross_width, layer=c_ll).put(-cross_length / 2, 0)
                nd.strt(length=cross_length, width=cross_width, layer=c_ll).put(0, +cross_width, -90)

                nd.strt(length=cross_length, width=cross_width, layer=c_ll).put(3 * cross_length / 2 + 2 * dist, 0)
                nd.strt(length=cross_length, width=cross_width, layer=c_ll).put(
                    -(2 * (3 / 2) * cross_length + dist) + 10, 0)

                nd.strt(length=cross_length, width=cross_width, layer=c_ll).put(0, +5 * cross_width + 2 * dist, -90)
                nd.strt(length=cross_length, width=cross_width, layer=c_ll).put(0, -3 * cross_width - 2 * dist, -90)
                # The other half part

                nd.strt(length=cross_length, width=cross_width, layer=c_ll1).put(cross_length / 2 + dist, 0)
                nd.strt(length=cross_length, width=cross_width, layer=c_ll1).put(-((3 / 2) * cross_length + dist), 0)

                nd.strt(length=cross_length, width=cross_width, layer=c_ll1).put(0, +3 * cross_width + dist, -90)
                nd.strt(length=cross_length, width=cross_width, layer=c_ll1).put(0, -cross_width - dist, -90)

                nd.strt(length=cross_length, width=cross_width, layer=c_ll1).put(0, +6 * cross_width + 4.5 * dist, -90)
                nd.strt(length=cross_length, width=cross_width, layer=c_ll1).put(0, -4 * cross_width - 4.5 * dist, -90)

                nd.strt(length=cross_length, width=cross_width, layer=c_ll1).put(5 * cross_length / 2 + 3 * dist, 0)
                nd.strt(length=cross_length, width=cross_width, layer=c_ll1).put(
                    -(3 * (3 / 2) * cross_length + dist) + 20, 0)
        nd.text(text = "1-2", height=200, layer = 'Planar Ring').put(-700-180-65,1800+300)
        nd.text(text = "1-2", height=200, layer = 'SiO').put(-700-180-65,1800+300)
        Left_Cross_Stn.put(-700-180,1500+300)
        nd.text(text = "2-3", height=200, layer = 'SiO').put(-65,1800+300)
        nd.text(text = "2-3", height=200, layer = 'Metal Rings').put(-65,1800+300)
        Mid_Cross_Stn.put(0,1500+300)
        nd.text(text = "3-4", height=200, layer = 'Metal Rings').put(880-65+230,1800+300)
        nd.text(text = "3-4", height=200, layer = 'N Metal').put(880-65+230,1800+300)
        Right_Cross_Stn.put(880+230,1500+300)
        nd.text(text="3-5", height=200, layer='Metal Rings').put(2*(880 + 230), 1800 + 300)
        nd.text(text="3-5", height=200, layer='Au plating ').put(2*(880 + 230), 1800 + 300)
        Extra_Right_Cross_Stn.put(2*(880+230),1500+300)

        with nd.Cell(name  = "Array_CTLMs") as Array_CTLM:
            outer_ring_r = 142
            gap_distance = 0
            gap_step = 5
            counter_goc = 0
            circle_reticle_layer = 'Metal Rings'
            goc = [8,12,16,20,25,30,35,40,50]
            for j in range(1,4):
                for i in range(1,4):
                    with nd.Cell(name = "CTLM{}".format(i)) as CTLM:
                        middle_circle_r = 50
                        cicrle_middle = nd.Polygon(layer=circle_reticle_layer, points=geom.circle(radius=middle_circle_r, N = 700)).put(0,0)
                        gap_distance = gap_distance + gap_step
                        inner_ring_r = middle_circle_r+ goc[counter_goc]
                        ring_width  = outer_ring_r-inner_ring_r
                        ring = nd.Polygon(layer=circle_reticle_layer, points=geom.ring(radius=outer_ring_r , width = ring_width , N = 700)).put(0,0)
                        Frame = Reticle.ret( 2*inner_ring_r , 2*inner_ring_r , outer_ring_r-inner_ring_r  , circle_reticle_layer)
                        counter_goc = counter_goc+1
                    CTLM.put((outer_ring_r)*2*i,-(outer_ring_r)*2*j) 
                    
                    
                    
                    
            #This is the box to remove the SiO and then apply the CTLM metal rings
            #nd.strt(length = 852 , width = 852, layer= 40 ).put(142,-568)
        Array_CTLM.put(-1300+1606-150+500-100,1700-2365+150+300+457+230/2)
        with nd.Cell(name="Array_CTLMs") as Array_CTLM_N_metal:
            outer_ring_r = 142
            gap_distance = 0
            gap_step = 5
            counter_goc = 0
            circle_reticle_layer = 'N Metal'
            goc = [8, 12, 16, 20, 25, 30, 35, 40, 50]
            for j in range(1, 4):
                for i in range(1, 4):
                    with nd.Cell(name="CTLM{}".format(i)) as CTLM:
                        middle_circle_r = 50
                        cicrle_middle = nd.Polygon(layer=circle_reticle_layer,
                                                   points=geom.circle(radius=middle_circle_r, N=700)).put(0, 0)
                        gap_distance = gap_distance + gap_step
                        inner_ring_r = middle_circle_r + goc[counter_goc]
                        ring_width = outer_ring_r - inner_ring_r
                        ring = nd.Polygon(layer=circle_reticle_layer,
                                          points=geom.ring(radius=outer_ring_r, width=ring_width, N=700)).put(0, 0)
                        Frame = Reticle.ret(2 * inner_ring_r, 2 * inner_ring_r, outer_ring_r - inner_ring_r,
                                            circle_reticle_layer)
                        counter_goc = counter_goc + 1
                    CTLM.put((outer_ring_r) * 2 * i, -(outer_ring_r) * 2 * j)

                    # This is the box to remove the SiO and then apply the CTLM metal rings
            # nd.strt(length = 852 , width = 852, layer= 40 ).put(142,-568)
        Array_CTLM_N_metal.put(-1300 + 1606 - 150 + 500 - 100+1200, 1700 - 2365 + 150 + 300 + 457 + 230 / 2)
        with nd.Cell(name = "Vernier pair") as Left_Vernier_Pair:
            with nd.Cell(name = "Vernier") as Horizaontal_Vernier:
                grod_length = 100
                grod_width = 20
                gnumber_of_rods = 12
                gletter_height = 3
                gdist_combs = 10-180
                
                vernier_1_layer_top = 'Planar Ring'
                v1lt = vernier_1_layer_top
                
                vernier_1_layer_bot = 'SiO'
                v1lb = vernier_1_layer_bot
                
                
                gHorVernCombTopRodDist= 40
                gHorVernCombBotRodDist= 40-0.5
                
                gVerVernCombTopRodDist= gHorVernCombTopRodDist
                gVerVernCombBotRodDist= gVerVernCombTopRodDist
                
                gdistnace_of_top_bot_combs_horiz = -80
                gdistnace_of_left_right_combs_ver = -3
                
                
                gx_correction_vert_letters = -3
                gy_correction_vert_letters = -2
                gx_correction_horiz_letters = -1
    
                #ONE HALF
                with nd.Cell(name = "HorVernTop") as HorVernTopGeert:
                    gr_rod_width = grod_width
            
                    with nd.Cell(name = "SeedComb2top") as SeedComb2topGeert:
                        for i in range(0,3):
                            gr_rod_width = grod_width*((1/2)**i)
                            nd.strt(length = grod_length, width = gr_rod_width, layer = v1lt).put()
                    with nd.Cell(name = "SeedComb2top") as SeedComb2topMid:
                        for i in range(0,3):
                            gr_rod_width = grod_width*((1/2)**i)
                            nd.strt(length = grod_length+0.4*grod_length, width = gr_rod_width, layer = v1lt).put()
                    SeedComb2topMid.put(0,0,-90)
                    for i in range(1,(gnumber_of_rods-1)//2+1):
                        SeedComb2topGeert.put(-gHorVernCombTopRodDist*i,0,-90)
                        SeedComb2topGeert.put(gHorVernCombTopRodDist*i,0,-90)
                HorVernTopGeert.put(0,0)
                #sECOND HALF
                with nd.Cell(name = "HorVernBot") as gHorVernBotGeert:
                    with nd.Cell(name = "SeedComb2Bot") as SeedComb2BotGeert:
            
                        nd.strt(length = 3*grod_length, width = grod_width, layer = v1lb).put()
    
                    for i in range(1,gnumber_of_rods//2+1):
                        SeedComb2BotGeert.put(-gHorVernCombBotRodDist*i-0.5/2+gHorVernCombTopRodDist/2,0,-90)
                        #nd.text("-{}".format(i), height=(gletter_height)).put(-gHorVernCombBotRodDist*i+gx_correction_horiz_letters+gHorVernCombTopRodDist/2,-3.2*grod_length+gdist_combs)
                        SeedComb2BotGeert.put(gHorVernCombBotRodDist*i+0.5/2-gHorVernCombTopRodDist/2,0,-90)
                        #nd.text("{}".format(i),height=(gletter_height)).put(gHorVernCombBotRodDist*i+gx_correction_horiz_letters-gHorVernCombTopRodDist/2,-3.2*grod_length+gdist_combs)
                gHorVernBotGeert.put(0,-3*grod_length-gdist_combs-gdistnace_of_top_bot_combs_horiz)
                nd.text("x", height=(200),layer=v1lb).put(1100-15+300-900-213-4.75,1800-60-1900-7)
                nd.text("0.5", height=(200), layer = v1lb).put(1100-15+300-900-213-4.75-280-110,1800-60-1900-7-431)
    
            Horizaontal_Vernier.put(0,0)
            
            
            
            with nd.Cell(name = "Vernier") as Vertical_Vernier:
                grod_length = 100
                grod_width = 20
                gnumber_of_rods = 12
                gletter_height = 3
                gdist_combs = 10-180
                
                vernier_1_layer_top = 'Planar Ring'
                v1lt = vernier_1_layer_top
                
                vernier_1_layer_bot = 'SiO'
                v1lb = vernier_1_layer_bot
                
                
                gHorVernCombTopRodDist= 40
                gHorVernCombBotRodDist= 40-0.5
                
                gVerVernCombTopRodDist= gHorVernCombTopRodDist
                gVerVernCombBotRodDist= gVerVernCombTopRodDist
                
                gdistnace_of_top_bot_combs_horiz = -80
                gdistnace_of_left_right_combs_ver = -3
                
                
                gx_correction_vert_letters = -3
                gy_correction_vert_letters = -2
                gx_correction_horiz_letters = -1
    
                #ONE HALF
                with nd.Cell(name = "HorVernTop") as HorVernTopGeert:
                    gr_rod_width = grod_width
            
                    with nd.Cell(name = "SeedComb2top") as SeedComb2topGeert:
                        for i in range(0,3):
                            gr_rod_width = grod_width*((1/2)**i)
                            nd.strt(length = grod_length, width = gr_rod_width, layer = v1lt).put()
                    with nd.Cell(name = "SeedComb2top") as SeedComb2topMid:
                        for i in range(0,3):
                            gr_rod_width = grod_width*((1/2)**i)
                            nd.strt(length = grod_length+0.4*grod_length, width = gr_rod_width, layer = v1lt).put()
                    SeedComb2topMid.put(0,0,-90)
                    for i in range(1,(gnumber_of_rods-1)//2+1):
                        SeedComb2topGeert.put(-gHorVernCombTopRodDist*i,0,-90)
                        SeedComb2topGeert.put(gHorVernCombTopRodDist*i,0,-90)
                HorVernTopGeert.put(0,0)
                #sECOND HALF
                with nd.Cell(name = "HorVernBot") as gHorVernBotGeert:
                    with nd.Cell(name = "SeedComb2Bot") as SeedComb2BotGeert:
            
                        nd.strt(length = 3*grod_length, width = grod_width, layer = v1lb).put()
    
                    for i in range(1,gnumber_of_rods//2+1):
                        SeedComb2BotGeert.put(-gHorVernCombBotRodDist*i-0.5/2+gHorVernCombTopRodDist/2,0,-90)
                        SeedComb2BotGeert.put(gHorVernCombBotRodDist*i+0.5/2-gHorVernCombTopRodDist/2,0,-90)
                        
                gHorVernBotGeert.put(0,-3*grod_length-gdist_combs-gdistnace_of_top_bot_combs_horiz)
                nd.text("y", height=(200),layer=v1lb).put(-367.25, -167)
                
                
     
                
            Horizaontal_Vernier.put(0,0)
            Vertical_Vernier.put(+600,-600,-90)
        with nd.Cell(name = "Vernier pair") as Mid_Vernier_Pair:
            with nd.Cell(name = "Vernier") as Horizaontal_Vernier:
                grod_length = 100
                grod_width = 20
                gnumber_of_rods = 12
                gletter_height = 3
                gdist_combs = 10-180
                
                vernier_1_layer_top = 'SiO'
                v1lt = vernier_1_layer_top
                
                vernier_1_layer_bot = 'Metal Rings'
                v1lb = vernier_1_layer_bot
                
                
                gHorVernCombTopRodDist= 40
                gHorVernCombBotRodDist= 40-0.5
                
                gVerVernCombTopRodDist= gHorVernCombTopRodDist
                gVerVernCombBotRodDist= gVerVernCombTopRodDist
                
                gdistnace_of_top_bot_combs_horiz = -80
                gdistnace_of_left_right_combs_ver = -3
                
                
                gx_correction_vert_letters = -3
                gy_correction_vert_letters = -2
                gx_correction_horiz_letters = -1
    
                #ONE HALF
                with nd.Cell(name = "HorVernTop") as HorVernTopGeert:
                    gr_rod_width = grod_width
            
                    with nd.Cell(name = "SeedComb2top") as SeedComb2topGeert:
                        for i in range(0,3):
                            gr_rod_width = grod_width*((1/2)**i)
                            nd.strt(length = grod_length, width = gr_rod_width, layer = v1lt).put()
                    with nd.Cell(name = "SeedComb2top") as SeedComb2topMid:
                        for i in range(0,3):
                            gr_rod_width = grod_width*((1/2)**i)
                            nd.strt(length = grod_length+0.4*grod_length, width = gr_rod_width, layer = v1lt).put()
                    SeedComb2topMid.put(0,0,-90)
                    for i in range(1,(gnumber_of_rods-1)//2+1):
                        SeedComb2topGeert.put(-gHorVernCombTopRodDist*i,0,-90)
                        SeedComb2topGeert.put(gHorVernCombTopRodDist*i,0,-90)
                HorVernTopGeert.put(0,0)
                #sECOND HALF
                with nd.Cell(name = "HorVernBot") as gHorVernBotGeert:
                    with nd.Cell(name = "SeedComb2Bot") as SeedComb2BotGeert:
            
                        nd.strt(length = 3*grod_length, width = grod_width, layer = v1lb).put()
    
                    for i in range(1,gnumber_of_rods//2+1):
                        SeedComb2BotGeert.put(-gHorVernCombBotRodDist*i-0.5/2+gHorVernCombTopRodDist/2,0,-90)
                        #nd.text("-{}".format(i), height=(gletter_height)).put(-gHorVernCombBotRodDist*i+gx_correction_horiz_letters+gHorVernCombTopRodDist/2,-3.2*grod_length+gdist_combs)
                        SeedComb2BotGeert.put(gHorVernCombBotRodDist*i+0.5/2-gHorVernCombTopRodDist/2,0,-90)
                        #nd.text("{}".format(i),height=(gletter_height)).put(gHorVernCombBotRodDist*i+gx_correction_horiz_letters-gHorVernCombTopRodDist/2,-3.2*grod_length+gdist_combs)
                gHorVernBotGeert.put(0,-3*grod_length-gdist_combs-gdistnace_of_top_bot_combs_horiz)
                nd.text("x", height=(200),layer=v1lb).put(1100-15+300-900-213-4.75,1800-60-1900-7)
                nd.text("0.5", height=(200), layer = v1lb).put(1100-15+300-900-213-4.75-280-110,1800-60-1900-7-431)
    
            Horizaontal_Vernier.put(0,0)
            
            
            
            with nd.Cell(name = "Vernier") as Vertical_Vernier:
                grod_length = 100
                grod_width = 20
                gnumber_of_rods = 12
                gletter_height = 3
                gdist_combs = 10-180
                
                vernier_1_layer_top = 'SiO'
                v1lt = vernier_1_layer_top
                
                vernier_1_layer_bot = 'Metal Rings'
                v1lb = vernier_1_layer_bot
                
                
                gHorVernCombTopRodDist= 40
                gHorVernCombBotRodDist= 40-0.5
                
                gVerVernCombTopRodDist= gHorVernCombTopRodDist
                gVerVernCombBotRodDist= gVerVernCombTopRodDist
                
                gdistnace_of_top_bot_combs_horiz = -80
                gdistnace_of_left_right_combs_ver = -3
                
                
                gx_correction_vert_letters = -3
                gy_correction_vert_letters = -2
                gx_correction_horiz_letters = -1
    
                #ONE HALF
                with nd.Cell(name = "HorVernTop") as HorVernTopGeert:
                    gr_rod_width = grod_width
            
                    with nd.Cell(name = "SeedComb2top") as SeedComb2topGeert:
                        for i in range(0,3):
                            gr_rod_width = grod_width*((1/2)**i)
                            nd.strt(length = grod_length, width = gr_rod_width, layer = v1lt).put()
                    with nd.Cell(name = "SeedComb2top") as SeedComb2topMid:
                        for i in range(0,3):
                            gr_rod_width = grod_width*((1/2)**i)
                            nd.strt(length = grod_length+0.4*grod_length, width = gr_rod_width, layer = v1lt).put()
                    SeedComb2topMid.put(0,0,-90)
                    for i in range(1,(gnumber_of_rods-1)//2+1):
                        SeedComb2topGeert.put(-gHorVernCombTopRodDist*i,0,-90)
                        SeedComb2topGeert.put(gHorVernCombTopRodDist*i,0,-90)
                HorVernTopGeert.put(0,0)
                #sECOND HALF
                with nd.Cell(name = "HorVernBot") as gHorVernBotGeert:
                    with nd.Cell(name = "SeedComb2Bot") as SeedComb2BotGeert:
            
                        nd.strt(length = 3*grod_length, width = grod_width, layer = v1lb).put()
    
                    for i in range(1,gnumber_of_rods//2+1):
                        SeedComb2BotGeert.put(-gHorVernCombBotRodDist*i-0.5/2+gHorVernCombTopRodDist/2,0,-90)
                        SeedComb2BotGeert.put(gHorVernCombBotRodDist*i+0.5/2-gHorVernCombTopRodDist/2,0,-90)
                        
                gHorVernBotGeert.put(0,-3*grod_length-gdist_combs-gdistnace_of_top_bot_combs_horiz)
                nd.text("y", height=(200),layer=v1lb).put(-367.25, -167)
                
                
     
                
            Horizaontal_Vernier.put(0,0)
            Vertical_Vernier.put(+600,-600,-90)
        with nd.Cell(name = "Vernier pair") as Right_Vernier_Pair:
            with nd.Cell(name = "Vernier") as Horizaontal_Vernier:
                grod_length = 100
                grod_width = 20
                gnumber_of_rods = 12
                gletter_height = 'Metal Rings'
                gdist_combs = 10-180
                
                vernier_1_layer_top = 'Metal Rings'
                v1lt = vernier_1_layer_top
                
                vernier_1_layer_bot = 'N Metal'
                v1lb = vernier_1_layer_bot
                
                
                gHorVernCombTopRodDist= 40
                gHorVernCombBotRodDist= 40-0.5
                
                gVerVernCombTopRodDist= gHorVernCombTopRodDist
                gVerVernCombBotRodDist= gVerVernCombTopRodDist
                
                gdistnace_of_top_bot_combs_horiz = -80
                gdistnace_of_left_right_combs_ver = -3
                
                
                gx_correction_vert_letters = -3
                gy_correction_vert_letters = -2
                gx_correction_horiz_letters = -1
    
                #ONE HALF
                with nd.Cell(name = "HorVernTop") as HorVernTopGeert:
                    gr_rod_width = grod_width
            
                    with nd.Cell(name = "SeedComb2top") as SeedComb2topGeert:
                        for i in range(0,3):
                            gr_rod_width = grod_width*((1/2)**i)
                            nd.strt(length = grod_length, width = gr_rod_width, layer = v1lt).put()
                    with nd.Cell(name = "SeedComb2top") as SeedComb2topMid:
                        for i in range(0,3):
                            gr_rod_width = grod_width*((1/2)**i)
                            nd.strt(length = grod_length+0.4*grod_length, width = gr_rod_width, layer = v1lt).put()
                    SeedComb2topMid.put(0,0,-90)
                    for i in range(1,(gnumber_of_rods-1)//2+1):
                        SeedComb2topGeert.put(-gHorVernCombTopRodDist*i,0,-90)
                        SeedComb2topGeert.put(gHorVernCombTopRodDist*i,0,-90)
                HorVernTopGeert.put(0,0)
                #sECOND HALF
                with nd.Cell(name = "HorVernBot") as gHorVernBotGeert:
                    with nd.Cell(name = "SeedComb2Bot") as SeedComb2BotGeert:
            
                        nd.strt(length = 3*grod_length, width = grod_width, layer = v1lb).put()
    
                    for i in range(1,gnumber_of_rods//2+1):
                        SeedComb2BotGeert.put(-gHorVernCombBotRodDist*i-0.5/2+gHorVernCombTopRodDist/2,0,-90)
                        #nd.text("-{}".format(i), height=(gletter_height)).put(-gHorVernCombBotRodDist*i+gx_correction_horiz_letters+gHorVernCombTopRodDist/2,-3.2*grod_length+gdist_combs)
                        SeedComb2BotGeert.put(gHorVernCombBotRodDist*i+0.5/2-gHorVernCombTopRodDist/2,0,-90)
                        #nd.text("{}".format(i),height=(gletter_height)).put(gHorVernCombBotRodDist*i+gx_correction_horiz_letters-gHorVernCombTopRodDist/2,-3.2*grod_length+gdist_combs)
                gHorVernBotGeert.put(0,-3*grod_length-gdist_combs-gdistnace_of_top_bot_combs_horiz)
                nd.text("x", height=(200),layer=v1lb).put(1100-15+300-900-213-4.75,1800-60-1900-7)
                nd.text("0.5", height=(200), layer = v1lb).put(1100-15+300-900-213-4.75-280-110,1800-60-1900-7-431)
            Horizaontal_Vernier.put(0,0)
            with nd.Cell(name = "Vernier") as Vertical_Vernier:
                grod_length = 100
                grod_width = 20
                gnumber_of_rods = 12
                gletter_height = 3
                gdist_combs = 10-180
                
                vernier_1_layer_top = 'Metal Rings'
                v1lt = vernier_1_layer_top
                
                vernier_1_layer_bot = 'N Metal'
                v1lb = vernier_1_layer_bot
                
                
                gHorVernCombTopRodDist= 40
                gHorVernCombBotRodDist= 40-0.5
                
                gVerVernCombTopRodDist= gHorVernCombTopRodDist
                gVerVernCombBotRodDist= gVerVernCombTopRodDist
                
                gdistnace_of_top_bot_combs_horiz = -80
                gdistnace_of_left_right_combs_ver = -3
                
                
                gx_correction_vert_letters = -3
                gy_correction_vert_letters = -2
                gx_correction_horiz_letters = -1
    
                #ONE HALF
                with nd.Cell(name = "HorVernTop") as HorVernTopGeert:
                    gr_rod_width = grod_width
            
                    with nd.Cell(name = "SeedComb2top") as SeedComb2topGeert:
                        for i in range(0,3):
                            gr_rod_width = grod_width*((1/2)**i)
                            nd.strt(length = grod_length, width = gr_rod_width, layer = v1lt).put()
                    with nd.Cell(name = "SeedComb2top") as SeedComb2topMid:
                        for i in range(0,3):
                            gr_rod_width = grod_width*((1/2)**i)
                            nd.strt(length = grod_length+0.4*grod_length, width = gr_rod_width, layer = v1lt).put()
                    SeedComb2topMid.put(0,0,-90)
                    for i in range(1,(gnumber_of_rods-1)//2+1):
                        SeedComb2topGeert.put(-gHorVernCombTopRodDist*i,0,-90)
                        SeedComb2topGeert.put(gHorVernCombTopRodDist*i,0,-90)
                HorVernTopGeert.put(0,0)
                #sECOND HALF
                with nd.Cell(name = "HorVernBot") as gHorVernBotGeert:
                    with nd.Cell(name = "SeedComb2Bot") as SeedComb2BotGeert:
            
                        nd.strt(length = 3*grod_length, width = grod_width, layer = v1lb).put()
    
                    for i in range(1,gnumber_of_rods//2+1):
                        SeedComb2BotGeert.put(-gHorVernCombBotRodDist*i-0.5/2+gHorVernCombTopRodDist/2,0,-90)
                        SeedComb2BotGeert.put(gHorVernCombBotRodDist*i+0.5/2-gHorVernCombTopRodDist/2,0,-90)
                        
                gHorVernBotGeert.put(0,-3*grod_length-gdist_combs-gdistnace_of_top_bot_combs_horiz)
                nd.text("y", height=(200),layer=v1lb).put(-367.25, -167)
            Horizaontal_Vernier.put(0,0)
            Vertical_Vernier.put(+600,-600,-90)
        with nd.Cell(name="Vernier pair") as Extra_Right_Vernier_Pair:
            with nd.Cell(name="Vernier") as Horizaontal_Vernier:
                grod_length = 100
                grod_width = 20
                gnumber_of_rods = 12
                gletter_height = 3
                gdist_combs = 10 - 180

                vernier_1_layer_top = 'Metal Rings'
                v1lt = vernier_1_layer_top

                vernier_1_layer_bot = 'Au plating '
                v1lb = vernier_1_layer_bot

                gHorVernCombTopRodDist = 40
                gHorVernCombBotRodDist = 40 - 0.5

                gVerVernCombTopRodDist = gHorVernCombTopRodDist
                gVerVernCombBotRodDist = gVerVernCombTopRodDist

                gdistnace_of_top_bot_combs_horiz = -80
                gdistnace_of_left_right_combs_ver = -3

                gx_correction_vert_letters = -3
                gy_correction_vert_letters = -2
                gx_correction_horiz_letters = -1

                # ONE HALF
                with nd.Cell(name="HorVernTop") as HorVernTopGeert:
                    gr_rod_width = grod_width

                    with nd.Cell(name="SeedComb2top") as SeedComb2topGeert:
                        for i in range(0, 3):
                            gr_rod_width = grod_width * ((1 / 2) ** i)
                            nd.strt(length=grod_length, width=gr_rod_width, layer=v1lt).put()
                    with nd.Cell(name="SeedComb2top") as SeedComb2topMid:
                        for i in range(0, 3):
                            gr_rod_width = grod_width * ((1 / 2) ** i)
                            nd.strt(length=grod_length + 0.4 * grod_length, width=gr_rod_width, layer=v1lt).put()
                    SeedComb2topMid.put(0, 0, -90)
                    for i in range(1, (gnumber_of_rods - 1) // 2 + 1):
                        SeedComb2topGeert.put(-gHorVernCombTopRodDist * i, 0, -90)
                        SeedComb2topGeert.put(gHorVernCombTopRodDist * i, 0, -90)
                HorVernTopGeert.put(0, 0)
                # sECOND HALF
                with nd.Cell(name="HorVernBot") as gHorVernBotGeert:
                    with nd.Cell(name="SeedComb2Bot") as SeedComb2BotGeert:
                        nd.strt(length=3 * grod_length, width=grod_width, layer=v1lb).put()

                    for i in range(1, gnumber_of_rods // 2 + 1):
                        SeedComb2BotGeert.put(-gHorVernCombBotRodDist * i - 0.5 / 2 + gHorVernCombTopRodDist / 2, 0,
                                              -90)
                        # nd.text("-{}".format(i), height=(gletter_height)).put(-gHorVernCombBotRodDist*i+gx_correction_horiz_letters+gHorVernCombTopRodDist/2,-3.2*grod_length+gdist_combs)
                        SeedComb2BotGeert.put(gHorVernCombBotRodDist * i + 0.5 / 2 - gHorVernCombTopRodDist / 2, 0, -90)
                        # nd.text("{}".format(i),height=(gletter_height)).put(gHorVernCombBotRodDist*i+gx_correction_horiz_letters-gHorVernCombTopRodDist/2,-3.2*grod_length+gdist_combs)
                gHorVernBotGeert.put(0, -3 * grod_length - gdist_combs - gdistnace_of_top_bot_combs_horiz)
                nd.text("x", height=(200), layer=v1lb).put(1100 - 15 + 300 - 900 - 213 - 4.75, 1800 - 60 - 1900 - 7)
                nd.text("0.5", height=(200), layer=v1lb).put(1100 - 15 + 300 - 900 - 213 - 4.75 - 280 - 110,
                                                             1800 - 60 - 1900 - 7 - 431)
            Horizaontal_Vernier.put(0, 0)
            with nd.Cell(name="Vernier") as Vertical_Vernier:
                grod_length = 100
                grod_width = 20
                gnumber_of_rods = 12
                gletter_height = 3
                gdist_combs = 10 - 180

                vernier_1_layer_top = 'Metal Rings'
                v1lt = vernier_1_layer_top

                vernier_1_layer_bot = 'Au plating '
                v1lb = vernier_1_layer_bot

                gHorVernCombTopRodDist = 40
                gHorVernCombBotRodDist = 40 - 0.5

                gVerVernCombTopRodDist = gHorVernCombTopRodDist
                gVerVernCombBotRodDist = gVerVernCombTopRodDist

                gdistnace_of_top_bot_combs_horiz = -80
                gdistnace_of_left_right_combs_ver = -3

                gx_correction_vert_letters = -3
                gy_correction_vert_letters = -2
                gx_correction_horiz_letters = -1

                # ONE HALF
                with nd.Cell(name="HorVernTop") as HorVernTopGeert:
                    gr_rod_width = grod_width

                    with nd.Cell(name="SeedComb2top") as SeedComb2topGeert:
                        for i in range(0, 3):
                            gr_rod_width = grod_width * ((1 / 2) ** i)
                            nd.strt(length=grod_length, width=gr_rod_width, layer=v1lt).put()
                    with nd.Cell(name="SeedComb2top") as SeedComb2topMid:
                        for i in range(0, 3):
                            gr_rod_width = grod_width * ((1 / 2) ** i)
                            nd.strt(length=grod_length + 0.4 * grod_length, width=gr_rod_width, layer=v1lt).put()
                    SeedComb2topMid.put(0, 0, -90)
                    for i in range(1, (gnumber_of_rods - 1) // 2 + 1):
                        SeedComb2topGeert.put(-gHorVernCombTopRodDist * i, 0, -90)
                        SeedComb2topGeert.put(gHorVernCombTopRodDist * i, 0, -90)
                HorVernTopGeert.put(0, 0)
                # sECOND HALF
                with nd.Cell(name="HorVernBot") as gHorVernBotGeert:
                    with nd.Cell(name="SeedComb2Bot") as SeedComb2BotGeert:
                        nd.strt(length=3 * grod_length, width=grod_width, layer=v1lb).put()

                    for i in range(1, gnumber_of_rods // 2 + 1):
                        SeedComb2BotGeert.put(-gHorVernCombBotRodDist * i - 0.5 / 2 + gHorVernCombTopRodDist / 2, 0,
                                              -90)
                        SeedComb2BotGeert.put(gHorVernCombBotRodDist * i + 0.5 / 2 - gHorVernCombTopRodDist / 2, 0, -90)

                gHorVernBotGeert.put(0, -3 * grod_length - gdist_combs - gdistnace_of_top_bot_combs_horiz)
                nd.text("y", height=(200), layer=v1lb).put(-367.25, -167)
            Horizaontal_Vernier.put(0, 0)
            Vertical_Vernier.put(+600, -600, -90)

        nd.text(text = "1-2", height=200, layer = 'Planar Ring').put(-700-180-65-200,1000+200)
        nd.text(text = "1-2", height=200, layer = 'SiO').put(-700-180-65-200,1000+200)
        Left_Vernier_Pair.put(-(400+150)-400-200,1000+200)
        nd.text(text = "2-3", height=200, layer = 'SiO').put(-65+86+(422-86)/2-(377-170)/2,1000+200)
        nd.text(text = "2-3", height=200, layer = 'Metal Rings').put(-65+86+(422-86)/2-(377-170)/2,1000+200)
        Mid_Vernier_Pair.put(-200+86+(422-86)/2-(377-170)/2,1000+200)
        nd.text(text = "3-4", height=200, layer = 'Metal Rings').put(880-65,1100-90+200)
        nd.text(text = "3-4", height=200, layer = 'N Metal').put(880-65,1100-90+200)
        Right_Vernier_Pair.put(400+150+500,1000+200)
        nd.text(text = "3-5", height=200, layer = 'Metal Rings').put(2*(880-65),1100-90+200)
        nd.text(text = "3-5", height=200, layer = 'Au plating ').put(2*(880-65),1100-90+200)
        Extra_Right_Vernier_Pair.put(2*(400+150+500),1000+200)






        with nd.Cell(name  = "Linewidth Module") as Linewidth_module:

            for i in range(4):
                line_length = 500
                step_lines = 370


                layer_names = ['Planar Ring', 'SiO', 'Metal Rings', 'Metal Ring Openings', 'N Metal' , 'Au plating ', 'lay22']
                if i==0 or i==1 or i==2:
                    nd.strt(length = line_length, width = 5, layer =layer_names[i]).put(0,-step_lines*i)
                    nd.text(text = '{}'.format(i+1), layer=layer_names[i], height=200).put(-150,-100 -step_lines*i)
                else:
                    nd.strt(length=line_length, width=5, layer=layer_names[i+1]).put(750, 1110-step_lines * i)
                    nd.text(text='{}'.format(i + 1), layer=layer_names[i+1], height=200).put(750-150,1110 -100 - step_lines * i)
        Linewidth_module.put(900+5000-7500+850/2, 1082-900)

        ###################################################
        ###################################################
        text_rotation = 0
        text_height = 180
        if Quadrant == 1:
            #nd.text("l{}um".format((1+extra_length/1000)), height= text_height).put(text_position_x, text_position_y,text_rotation)
            
            nd.text("R{}C{}Q{}".format((row_ID),(column_ID),(1)), height= text_height, layer='Au plating ').put(text_position_x, text_position_y_layer_ID,text_rotation)

        elif Quadrant == 2:
            #nd.text("l{}um".format((1+extra_length/1000)), height= text_height).put(text_position_x, text_position_y,text_rotation)
            nd.text("R{}C{}Q{}".format((row_ID),(column_ID),(2)), height= text_height, layer='Au plating ').put(text_position_x, text_position_y_layer_ID,text_rotation)

        elif Quadrant ==3:
            #nd.text("l{}um".format((1+extra_length/1000)), height= text_height).put(text_position_x, text_position_y,text_rotation)
            nd.text("R{}C{}Q{}".format((row_ID),(column_ID),(3)), height= text_height, layer='Au plating ').put(text_position_x, text_position_y_layer_ID,text_rotation)

        else:
            #nd.text("l{}um".format((1+extra_length/1000)), height= text_height).put(text_position_x, text_position_y,text_rotation)
            nd.text("R{}C{}Q{}".format((row_ID),(column_ID),(4)), height= text_height, layer='Au plating ').put(text_position_x, text_position_y_layer_ID,text_rotation)


        
        nd.text("VTEC", height =text_height, layer= 'Au plating ' ).put(1000-300+text_position_x ,text_position_y_layer_ID,0)
        
        
        
        def matrix_of_bars(layer_bars):
            with nd.Cell(name = "Matrix of bars") as matrix_of_bars:
                if layer_bars == 'Au plating ' or layer_bars == 'Metal Rings' or layer_bars == 'N Metal':
                    layerN = 200
                else:
                    layerN = 0
                for j in range(0,3):
                    with nd.Cell(name = "test cell") as test_cell:
                        column_distances = [100, 625, 1250]
                        test_width  = 5
                        distance  =  100*(j+1)
                        width_of_metal_pad = 100
                        length_of_metal_pad = 100
                        layer = layer_bars
                        with nd.Cell(name="Metal pad") as metal_pad:
                            nd.strt(width= width_of_metal_pad , length  = length_of_metal_pad , layer = layer).put()
                            
                        with nd.Cell(name = "Clumn of bars") as Column_of_bars:
                            
                            number_of_bars_variation_in_width = 4
                            nobviw = number_of_bars_variation_in_width 
                            wwv= [5,10,20,50]
                            for i in range(nobviw):
                                yy = (200+175+width_of_metal_pad)*i-layerN
                                
                                nd.text("{},{}".format(wwv[i], distance), layer = layer).put(0, yy+50,0)
    
                                metal_pad.put(-length_of_metal_pad  , yy )
                                metal_pad.put(distance, yy )
                                nd.strt(width = wwv[i], length  = distance , layer = layer).put(0, yy )
                        Column_of_bars.put()
                    # test_cell.put(100*(j+1)+(600-layerN)*j,0)
                    test_cell.put(column_distances[j],0)
                    print(100*(j+1)+(600-layerN)*j)
                if layer == 'Metal Rings':
                    nd.text("Ti/Pt/Au", height= 100, layer = layer).put(270,+850-33+500,0)
                elif layer=='N Metal':
                    nd.text("Ni/Ge/Au",height= 30, layer=layer).put(270, +850-33, 0)
                else:
                    nd.text("Au plating", height= 100, layer = layer).put(190,+850-33+500)
            return matrix_of_bars
                
        Bars1 = matrix_of_bars('Metal Rings').put(-1750+150,-1812-238-50,0)
        # Bars2 = matrix_of_bars('N Metal').put(-150,-1812,0)
        Bars3 = matrix_of_bars('Au plating ').put(1450-200-238+50+188,-50-1812-238,0)

        
        
        cover_one_layer = 'MESA etch'
        with nd.Cell(name = "Cover 1") as Cover_one:
            
            
            
            nd.strt(length = 4700-1150, width  = 1105, layer = cover_one_layer).put(-1800+1150, -222.5)
            nd.strt(length = 1150, width  = 1105-265, layer = cover_one_layer).put(-1800, -222.5-265/2)


            nd.strt(length = 2250+2450, width  = 2780-1105, layer = cover_one_layer).put(-1800,-50-1050+40-1105/2)
            

        Cover_one.put(0,0)
        cover_two_layer = 'SiO'
        with nd.Cell(name = "Cover 2") as Cover_two:
            nd.strt(length = 2250+2450, width  = 1380+108-13+200, layer = cover_two_layer).put(-1800,-1050+40-600+225/2-50-12.5+108/2-13/2-100)
            #nd.strt(length = 2025+2450, width  = 225-25, layer = cover_two_layer).put(-1800+225,-1050+40-600+225/2-740-100-12.5)
            nd.strt(length = 2250-1150, width  = 2600+80-660-828+10-108-2+13, layer = cover_two_layer).put(-1800+1150,-1200-1050+40+3000-650-828/2+5+108/2-1-13/2)
        Cover_two.put(0,0)
        ###########METAL CORNERS#######
        ######Metal Corners
        top_left = metal_corners.Metal_corners('Metal Rings').put(-1000 + 115-865-25, 4279.86 + 0.14-1830, -90)
        top_left_hole = metal_corners.Metal_corners_hole('Open Corners').put(-1000 + 115 + 200 - 50-865, 4279.86 + 0.14 - 200-1830,
                                                                        90)

        top_right = metal_corners.Metal_corners('Metal Rings').put(1000 + 65+3835, +4230-1830+25, 180)
        top_right_hole = metal_corners.Metal_corners_hole('Open Corners').put(1000 + 65 - 200+3835, +4230 - 150-1830, 0)

        bot_right = metal_corners.Metal_corners('Metal Rings').put(-1000 + 2015+3835+25, -1000 + 430 - 50-1830, 90)
        bot_right_hole = metal_corners.Metal_corners_hole('Open Corners').put(-1000 + 2015 - 200 + 50+3835,
                                                                         -1000 + 430 - 50 + 200-1830, -90)

        bot_left = metal_corners.Metal_corners('Metal Rings').put(-1000 + 65-865, 430 - 1000-1830-25)
        bot_left_hole = metal_corners.Metal_corners_hole('Open Corners').put(-1000 + 65 + 200-865-25, 430 - 1000 + 150-1830-200, 90)

        Layer_Difference('Open Corners', 'SiO', Single_Tile)
        Dark_Current_PCM_V3.PCM_Dark_Current_Planar(extra_length=0, Quadrant=Quadrant, i=1, j=1, show_name= False, show_frame = False).put(3850-15,-1830)
        
    return Single_Tile


def merge_polygons(cell, layers):
    """Merge all polygons per layer after flattening <cell>.

    Cell <cell> itself will not be affected. Note that a merged polygons may
    still consist of multiple polygons (islands).

    Args:
        cell (Cell): cell to process
        layers (list of str): names of layers to merge polygons in

    Returns:
        dict: {layer_name: merged_polygon}
    """
    pgons = defaultdict(list)
    for params in nd.cell_iter(cell, flat=True):
        for pgon, xy, bbox in params.iters['polygon']:
            for lay in layers:
                if pgon.layer == lay:
                    pgons[lay].append(xy)
    for lay in layers:
        pgons[lay] = nd.clipper.merge_polygons(pgons[lay])
    return pgons

def remove_polygons(cell, layers):
    """Remove all polygons in <layers> from <cell>.

    Args:
        cell (Cell): cell to process
        layers (list of str): names of layers to delete polygons from

    Returns:
        None
    """
    for params in nd.cell_iter(cell):
        if params.cell_start:
            pgons = []
            for pgon in params.cell.polygons:
                if pgon[1].layer not in layers:
                    pgons.append(pgon)
            params.cell.polygons = pgons
    return None

def Layer_Difference(Remove_layer,From_layer,cell_name):

    pgons = merge_polygons(cell=cell_name, layers=[Remove_layer, From_layer])
    remove_polygons(cell=cell_name, layers=[Remove_layer, From_layer])  # optional
    pdiff = nd.clipper.diff_polygons(pgons[From_layer], pgons[Remove_layer])
    for pol in pdiff:
        nd.Polygon(points=pol, layer=From_layer).put(0)
    nd.netlist.pin2pin_drc_off()
    return cell_name






if __name__ == "__main__":

    i = 1 
    j = 3
    Q1 = 1
    Tile_PCMs_all(0, Q1, i,j).put()


# =============================================================================
# nd.strt(length  = 100000 , width = 0.1, layer = 1).put(-100000/2,0)
# nd.strt(width  = 100000 , length = 0.1, layer = 1).put(0,0)
# =============================================================================

    nd.export_gds(filename=r'Mask_GDS/Tile PCMS V2 N Substrate') 