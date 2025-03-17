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
# from MZmodulator import *
import nazca.geometries as geom
import metal_corners
from collections import defaultdict


def Tile_APD_length(extra_length, Quadrant, i,j, show_name):
    
    

    
    
    metal_pads_layer = 50



    
    x_move = +300-7.5-151.25-250
    y_move = -1150-700
    with nd.Cell(name = 'One tile') as Single_Tile:

        nd.add_layer(name='lay2', layer=2, accuracy=0.001)
        nd.add_layer(name='lay22', layer=22, accuracy=0.001)
        nd.add_layer(name='lay5', layer=5, accuracy=0.001)
        ######## All fixed here don't change ##############
        frame_length = 2000
        frame_width = 4900
        fram_cut_area = 100
        if show_name:
            Frame_for_tile.frafrafra(frame_length + extra_length , frame_width, fram_cut_area, 1).put(-frame_length/2 -extra_length/2+300 -250  , -frame_width/2)
            Frame_for_tile.frafrafra(frame_length + extra_length , frame_width, fram_cut_area, 2).put(-frame_length/2 -extra_length/2+300 -250  , -frame_width/2)
        width_wvg = 1.5
        text_position_x = -extra_length/2-1345+200+500
        text_position_y =1328.625
        text_position_y_layer_ID = -745
        text_rotation = -90
        text_height = 200
        with nd.Cell(name = "Rings for Metal") as Rings:
            width_ring = 25
            radius1 = 80+width_ring
            radius2 = 100+width_ring
            radius3 = 150+width_ring
            radius4 = 200+width_ring
            radius5 = 250+width_ring
            extra_dist_rings = 550
            
            
           
            thickness = 15
            
            
            ring1 = nd.Polygon(layer=3, points=geom.ring(radius=radius1, width =width_ring , N = 700)).put(0,0)
            
            
            ring1 = nd.Polygon(layer='lay2', points=geom.circle(radius=radius1-width_ring+5 , N = 700)).put()
            ring1 = nd.Polygon(layer='lay2', points=geom.ring(radius=radius1+100+100, width =200+5, N = 700)).put(0,0)
            
            nd.strt(length=590-36+341+655+25, width = 402.5-20+100, layer=2).put(-311.25+36-341, -298.75-10-50)
            


            ring2 = nd.Polygon(layer=3, points=geom.ring(radius=radius2, width =width_ring, N = 700)).put(0,radius1+radius2+extra_dist_rings)
            ring1 = nd.Polygon(layer='lay2', points=geom.circle(radius=radius2-width_ring +5, N = 700)).put(0,radius1+radius2+extra_dist_rings)
            ring2 = nd.Polygon(layer='lay2', points=geom.ring(radius=radius2+100+100, width =100+100+5, N = 700)).put(0,radius1+radius2+extra_dist_rings)
            
            
            
            nd.strt(length=590-36, width = 600-5-80, layer='lay2').put(-311.25+36,397.5-20)


            
            ring3 = nd.Polygon(layer=3, points=geom.ring(radius=radius3, width =width_ring, N = 700)).put(0,(radius1+2*radius2)+radius3+2*extra_dist_rings)
            ring1 = nd.Polygon(layer='lay2', points=geom.circle(radius=radius3-width_ring+5 , N = 700)).put(0,(radius1+2*radius2)+radius3+2*extra_dist_rings)
            ring3 = nd.Polygon(layer='lay2', points=geom.ring(radius=radius3+100+100, width =100+100+5, N = 700)).put(0,(radius1+2*radius2)+radius3+2*extra_dist_rings)
            
            
            
            nd.strt(length=590-36, width = 600-5-180+20, layer='lay2').put(-311.25+36,1232.5-70)

            
            ring4 = nd.Polygon(layer=3, points=geom.ring(radius=radius4, width =width_ring, N = 700)).put(0,radius1+2*radius2+2*radius3 +radius4+3*extra_dist_rings)
            ring1 = nd.Polygon(layer='lay2', points=geom.circle(radius=radius4-width_ring+5 , N = 700)).put(0,radius1+2*radius2+2*radius3 +radius4+3*extra_dist_rings)
            ring4 = nd.Polygon(layer='lay2', points=geom.ring(radius=radius4+100+100, width =100+100+5, N = 700)).put(0,radius1+2*radius2+2*radius3 +radius4+3*extra_dist_rings)
            
            
            nd.strt(length=590-36, width = 500-5+50+50-5-200, layer='lay2').put(-311.25+36,2165-60-30)

            
            ring5 = nd.Polygon(layer=3, points=geom.ring(radius=radius5, width =width_ring, N = 700)).put(0,radius1+2*radius2+2*radius3+2*radius4+radius5+4*extra_dist_rings)
            ring1 = nd.Polygon(layer='lay2', points=geom.circle(radius=radius5-width_ring +5, N = 700)).put(0,radius1+2*radius2+2*radius3+2*radius4+radius5+4*extra_dist_rings)
            ring5 = nd.Polygon(layer='lay2', points=geom.ring(radius=radius5+80+150, width =80+150+5, N = 700)).put(0,radius1+2*radius2+2*radius3+2*radius4+radius5+4*extra_dist_rings)


            bot_box = nd.strt(length=590-36, width = 500-5+50+50-5-100+70+10-200, layer='lay2').put(-311.25+36,3215-150)

            nd.strt(length=590-36+341+655+25, width = 100+10+50+65+100, layer='lay2').put(-341-311.25+36-25,-475+402.5/2-25+600+100-3.75+600+200+35+900+50-20+2.5+1000+50+1100+10-500+250+20+25-65/2+50)
            
            #These are the white TRIAGNLEs

            nd.strt(length = 1000-120-100-100-25, width = 4700-200-250, layer  = 'lay2').put(158.75+300-180,+1850)
            nd.strt(length = 225, width = 4700-200-250+25+175+25, layer  = 'lay2').put(158.75+300-180+655,+1850+25/2)


            
            
            nd.strt(length = 1000-120+250+40-4-600-100-125, width = 4700-200-250, layer  = 'lay2').put(-1441.25+660+100-60+125,+1850)
            
            nd.strt(length = 1000-120+250+40-4-600-100-125-116, width = 4700-200-250+25+175+25, layer  = 'lay2').put(-1441.25+660+100-60+125-225,12.5+1850-25)
        Rings.put(x_move,y_move)
        plating_layer = 5
        with nd.Cell(name = "Plating") as Plating:
            length_plating = 706.25
            plating_wdith = 80
            fraction_overlap = 0.90
            ring1 = nd.strt(layer= plating_layer, length = length_plating+radius5-radius1, width = plating_wdith ).put(radius1-width_ring*fraction_overlap,0)
            ring2 = nd.strt(layer= plating_layer, length = length_plating+radius5-radius2, width = plating_wdith).put(radius2-width_ring*fraction_overlap,radius1+radius2+extra_dist_rings)
            ring3 = nd.strt(layer= plating_layer, length = length_plating+radius5-radius3, width = plating_wdith).put(radius3-width_ring*fraction_overlap,(radius1+2*radius2)+radius3+2*extra_dist_rings)
            ring4 = nd.strt(layer= plating_layer, length = length_plating+radius5-radius4, width = plating_wdith).put(radius4-width_ring*fraction_overlap,radius1+2*radius2+2*radius3 +radius4+3*extra_dist_rings)
            ring5 = nd.strt(layer= plating_layer, length = length_plating, width = plating_wdith).put(radius5-width_ring*fraction_overlap,radius1+2*radius2+2*radius3+2*radius4+radius5+4*extra_dist_rings)
        Plating.put(x_move,y_move)
        with nd.Cell(name = "Ring ID") as Ring_ID:
            length_plating = 700
            plating_wdith = 80
            ring1 = nd.text( "r{}".format(int(radius1-width_ring)) , layer='lay5', height= text_height).put(-radius1+width_ring/2-600,-text_height/2-150+240,90)
            ring2 = nd.text( "r{}".format(int(radius2-width_ring)) , layer='lay5', height= text_height).put(-radius2+width_ring/2-600,radius1+radius2+extra_dist_rings-text_height/2-130+150, 90)
            ring3 = nd.text( "r{}".format(int(radius3-width_ring)) , layer='lay5', height= text_height).put(-radius3+width_ring/2-600,(radius1+2*radius2)+radius3+2*extra_dist_rings-text_height/2-84 +75, 90)
            ring4 = nd.text( "r{}".format(int(radius4-width_ring)) , layer='lay5', height= text_height).put(-radius4+width_ring/2-600,radius1+2*radius2+2*radius3 +radius4+3*extra_dist_rings-text_height/2-35 +50, 90)
            ring5 = nd.text( "r{}".format(int(radius5-width_ring)) , layer='lay5', height= text_height).put(-radius5+width_ring/2-600,radius1+2*radius2+2*radius3+2*radius4+radius5+4*extra_dist_rings-text_height/2+15, 90)
        Ring_ID.put(x_move+650-270,y_move+400-550)
        with nd.Cell(name = "P connection") as P_connection:
            
            RF_ground = False
            RF_ground_layer = 'lay5'
            RF_ground_layer_openings = 'lay22'
            RF_ground_layer_openings_Nmetal = 4
            length_plating = 700
            plating_wdith = 80
            
            
            ring1 = nd.strt(layer= plating_layer, length = 200, width = 200 ).put(length_plating+radius5-radius1+87.5,0)
            ring2 = nd.strt(layer= plating_layer, length = 200, width = 200).put(length_plating+radius5-radius2+radius2-width_ring/2-5,radius1+radius2+extra_dist_rings)
            ring3 = nd.strt(layer= plating_layer, length =200, width = 200).put(length_plating+radius5-radius3+radius3-width_ring/2-5,(radius1+2*radius2)+radius3+2*extra_dist_rings)
            ring4 = nd.strt(layer= plating_layer, length =200, width = 200).put(length_plating+radius5-radius4+radius4-width_ring/2-5,radius1+2*radius2+2*radius3 +radius4+3*extra_dist_rings)
            ring5 = nd.strt(layer= plating_layer, length = 200, width = 200).put(length_plating+radius5-width_ring/2-5,radius1+2*radius2+2*radius3+2*radius4+radius5+4*extra_dist_rings)

            if RF_ground:
                ring_positions = [(0, 0),
                                  (0, radius1 + radius2 + extra_dist_rings),
                                  (0, (radius1 + 2 * radius2) + radius3 + 2 * extra_dist_rings),
                                  (0, radius1 + 2 * radius2 + 2 * radius3 + radius4 + 3 * extra_dist_rings),
                                  (0,
                                   radius1 + 2 * radius2 + 2 * radius3 + 2 * radius4 + radius5 + 4 * extra_dist_rings)]

                extra_length_ground_rf = 120
                ring_radius_rf = [80+extra_length_ground_rf,100+extra_length_ground_rf,150+extra_length_ground_rf,200+extra_length_ground_rf,250+extra_length_ground_rf]
                rf_metals_width  = 80
                rf_extra_dist = 0

                angles = [105, 111, 123, 131, 137] # This is for changing the distance of the power lines of the GSG
                length_of_the_main_straight_line = [230+6.15,206+6,148+5.7,94+3.9,40+3.8]
                trapezoid_height  = 100
                bond_pad_size = 200
                ii =0
                for position in ring_positions:
                    sbend_angle_rf = 45
                    radius_of_the_second_rf = 300
                    put1x = ring_radius_rf[ring_positions.index(position)]
                    put2x = -put1x
                    angle = angles[ring_positions.index(position)]

                    with nd.Cell(name="Rf Metal Rings") as Rf_metal_rings:
                        with nd.Cell(name="Rf Metal Rings Up") as Rf_metal_rings_up:
                            N_contact_ring_top = nd.bend(angle=angle, radius= put1x , width=rf_metals_width, offset=0,
                                                       layer=RF_ground_layer).put(put1x, 0, 90)
                            bend_rf_top = nd.bend(radius = 50, width = rf_metals_width, angle  = -(angle-90)-(180-angle)/2, layer = RF_ground_layer).put(N_contact_ring_top.pin["a0"],flip = True)
                            nd.strt(length = length_of_the_main_straight_line[ring_positions.index(position)], width = rf_metals_width, layer  = RF_ground_layer).put()
                            bend_after_strt = nd.bend(angle = sbend_angle_rf, radius = radius_of_the_second_rf, width = rf_metals_width, offset = 0, layer = RF_ground_layer).put()
                            nd.bend(angle = sbend_angle_rf, radius = radius_of_the_second_rf, width = rf_metals_width, offset = 0, layer = RF_ground_layer).put(bend_after_strt.pin["b0"],flip= True)
                            trapezoid_connection  = Trapezoid_Electric_Pads(trapezoid_height,rf_metals_width, bond_pad_size, RF_ground_layer).put()
                            nd.strt(length  = bond_pad_size, width = bond_pad_size, layer = RF_ground_layer ).put(trapezoid_connection.pin["Pin_Connection_Electrodes_Pads_right_side"])
                            termination_Rf_ring = nd.bend(radius = put1x, width = rf_metals_width, angle  = 180-angle, layer = RF_ground_layer).put(N_contact_ring_top.pin["b0"])

                        Rf_metal_rings_up.put(0, 0)
                        with nd.Cell(name="Rf Metal Rings Down") as Rf_metal_rings_down:
                            N_contact_ring_bot = nd.bend(angle=angle, radius=put1x, width=rf_metals_width, offset=0,
                                                       layer=RF_ground_layer).put(
                                put2x, 0, -90)
                            bend_rf_top = nd.bend(radius = 50, width = rf_metals_width, angle  = -(angle-90)-(180-angle)/2, layer = RF_ground_layer).put(N_contact_ring_bot.pin["b0"],flip = False)
                            strt_after_ring_rf = nd.strt(length = length_of_the_main_straight_line[ring_positions.index(position)], width = rf_metals_width, layer  = RF_ground_layer).put()
                            bend_after_strt = nd.bend(angle=sbend_angle_rf, radius=radius_of_the_second_rf,
                                                      width=rf_metals_width, offset=0, layer=RF_ground_layer).put(strt_after_ring_rf.pin["b0"],flip = True)
                            nd.bend(angle=sbend_angle_rf, radius=radius_of_the_second_rf, width=rf_metals_width,
                                    offset=0, layer=RF_ground_layer).put(bend_after_strt.pin["b0"])
                            trapezoid_connection = Trapezoid_Electric_Pads(trapezoid_height, rf_metals_width,
                                                                           bond_pad_size, RF_ground_layer).put()
                            nd.strt(length=bond_pad_size, width=bond_pad_size, layer=RF_ground_layer).put(
                                trapezoid_connection.pin["Pin_Connection_Electrodes_Pads_right_side"])

                            #straight_line_rf_bot = nd.strt(length = 100, width = rf_metals_width).put(N_contact_ring_bot.pin("b0"))

                        Rf_metal_rings_down.put(0, 0, 0)
                    Rf_metal_rings.put(0, position[1], (180 - angle) / 2)

                    with nd.Cell(name="Rf Metal Rings Openings") as Rf_metal_rings_openings:
                        with nd.Cell(name="Rf Metal Rings Openings Up") as Rf_metal_rings_openings_up:
                            N_contact_ring_top = nd.bend(angle=angle, radius= put1x , width=rf_metals_width, offset=0,
                                                       layer=RF_ground_layer_openings).put(put1x, 0, 90)
                            bend_rf_top = nd.bend(radius = 50, width = rf_metals_width, angle  = -(angle-90)-(180-angle)/2, layer = RF_ground_layer_openings).put(N_contact_ring_top.pin["a0"],flip = True)
                            termination_Rf_ring = nd.bend(radius = put1x, width = rf_metals_width, angle  = 180-angle, layer = RF_ground_layer_openings).put(N_contact_ring_top.pin["b0"])

                        Rf_metal_rings_openings_up.put(0, 0)
                        with nd.Cell(name="Rf Metal Rings Openings Down") as Rf_metal_rings_openings_down:
                            N_contact_ring_bot = nd.bend(angle=angle, radius=put1x, width=rf_metals_width, offset=0,
                                                       layer=RF_ground_layer_openings).put(
                                put2x, 0, -90)
                            bend_rf_top = nd.bend(radius = 50, width = rf_metals_width, angle  = -(angle-90)-(180-angle)/2, layer = RF_ground_layer_openings).put(N_contact_ring_bot.pin["b0"],flip = False)


                        Rf_metal_rings_openings_down.put(0, 0, 0)
                    Rf_metal_rings_openings.put(0, position[1], (180 - angle) / 2)

                    with nd.Cell(name="Rf Metal Rings Openings") as Rf_metal_rings_openings_Nmetal:
                        with nd.Cell(name="Rf Metal Rings Openings Up") as Rf_metal_rings_openings_up:
                            N_contact_ring_top = nd.bend(angle=angle, radius= put1x , width=rf_metals_width, offset=0,
                                                       layer=RF_ground_layer_openings_Nmetal).put(put1x, 0, 90)
                            bend_rf_top = nd.bend(radius = 50, width = rf_metals_width, angle  = -(angle-90)-(180-angle)/2, layer = RF_ground_layer_openings_Nmetal).put(N_contact_ring_top.pin["a0"],flip = True)
                            termination_Rf_ring = nd.bend(radius = put1x, width = rf_metals_width, angle  = 180-angle, layer = RF_ground_layer_openings_Nmetal).put(N_contact_ring_top.pin["b0"])

                        Rf_metal_rings_openings_up.put(0, 0)
                        with nd.Cell(name="Rf Metal Rings Openings Down") as Rf_metal_rings_openings_down:
                            N_contact_ring_bot = nd.bend(angle=angle, radius=put1x, width=rf_metals_width, offset=0,
                                                       layer=RF_ground_layer_openings_Nmetal).put(
                                put2x, 0, -90)
                            bend_rf_top = nd.bend(radius = 50, width = rf_metals_width, angle  = -(angle-90)-(180-angle)/2, layer = RF_ground_layer_openings_Nmetal).put(N_contact_ring_bot.pin["b0"],flip = False)


                        Rf_metal_rings_openings_down.put(0, 0, 0)
                    Rf_metal_rings_openings_Nmetal.put(0, position[1], (180 - angle) / 2)

        P_connection.put(x_move+1.25,y_move)
        with nd.Cell(name = "Semiconductor Etch") as Semiconductor_Etch:

            Semiconductor_Etch_Layer = 1
            ring1 = nd.Polygon(layer=Semiconductor_Etch_Layer, points=geom.circle(radius=radius1+30, N = 700)).put(0,0)
            ring2 = nd.Polygon(layer=Semiconductor_Etch_Layer, points=geom.circle(radius=radius2+30, N = 700)).put(0,radius1+radius2+extra_dist_rings)
            ring3 = nd.Polygon(layer=Semiconductor_Etch_Layer, points=geom.circle(radius=radius3+30, N = 700)).put(0,(radius1+2*radius2)+radius3+2*extra_dist_rings)
            ring4 = nd.Polygon(layer=Semiconductor_Etch_Layer, points=geom.circle(radius=radius4+30, N = 700)).put(0,radius1+2*radius2+2*radius3 +radius4+3*extra_dist_rings)
            ring5 = nd.Polygon(layer=Semiconductor_Etch_Layer, points=geom.circle(radius=radius5+30, N = 700)).put(0,radius1+2*radius2+2*radius3+2*radius4+radius5+4*extra_dist_rings)
        Semiconductor_Etch.put(x_move,y_move)
        if show_name:
            with nd.Cell("Wafer ID") as wafer_id:
                if Quadrant == 1:
                    #nd.text("l{}um".format((1+extra_length/1000)), height= text_height).put(text_position_x, text_position_y,text_rotation)

                    nd.text("R{}C{}Q{}".format((j+1),(i+1),(1)), height= text_height, layer="lay5").put(text_position_x, text_position_y_layer_ID,text_rotation)

                elif Quadrant == 2:
                    #nd.text("l{}um".format((1+extra_length/1000)), height= text_height).put(text_position_x, text_position_y,text_rotation)
                    nd.text("R{}C{}Q{}".format((j+1),(i+1),(2)), height= text_height, layer='lay5').put(text_position_x, text_position_y_layer_ID,text_rotation)

                elif Quadrant ==3:
                    #nd.text("l{}um".format((1+extra_length/1000)), height= text_height).put(text_position_x, text_position_y,text_rotation)
                    nd.text("R{}C{}Q{}".format((j+1),(i+1),(3)), height= text_height, layer='lay5').put(text_position_x, text_position_y_layer_ID,text_rotation)

                else:
                    #nd.text("l{}um".format((1+extra_length/1000)), height= text_height).put(text_position_x, text_position_y,text_rotation)
                    nd.text("R{}C{}Q{}".format((j+1),(i+1),(4)), height= text_height, layer='lay5').put(text_position_x, text_position_y_layer_ID,text_rotation)




                nd.text("VTEC", height =text_height, layer= 'lay5' ).put(text_position_x ,text_position_y_layer_ID+800,-90)
            wafer_id.put(-1370,0, 180)

        metal_corners.Metal_corners(False).put(1000,-2300-50-100,90)
        metal_corners.Metal_corners(True).put(1000+50,4650-2300-50+100,180)
        if show_name:
            metal_corners.Metal_corners(True).put(-950,-2300-100)
            metal_corners.Metal_corners(True).put(1000+50-1950,4650-2300-50+50+100,270)
        else:
            nd.strt(width= 200 , length= 225, layer= 'lay2').put(-950,-2300-50)
            nd.strt(width= 200 , length= 225, layer= 'lay2').put(1000+50-1950+50,4650-2300-50+50+100,270)

        if RF_ground:

            I = 'Inverted'
            pgons = merge_polygons(cell=Single_Tile, layers=['lay22', 'lay2'])
            remove_polygons(cell=Single_Tile, layers=['lay22', 'lay2'])  # optional
            pdiff = nd.clipper.diff_polygons(pgons['lay2'], pgons['lay22'])
            for pol in pdiff:
                nd.Polygon(points=pol, layer='lay2').put(0)
            nd.netlist.pin2pin_drc_off()

    return Single_Tile
def Trapezoid_Electric_Pads(height, side1, side2,layer):
    with nd.Cell(name='Trapezoid Connection Electrodes Pads') as Trapezoid_Connection_Electrodes_Pads:
        pipes = nd.Polygon(layer=layer, points=[(0, side1 / 2), (0, -side1 / 2),
                                                           (height, -side2 / 2 ),
                                                           (height, side2 / 2 )])
        pipes.put(0, 0)
        nd.Pin(name="Pin_Connection_Electrodes_Pads_right_side").put(height, 0)
        nd.Pin(name="Pin_Connection_Electrodes_Pads_left_side").put(0, 0)


    return Trapezoid_Connection_Electrodes_Pads

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

i = 1 
j = 3
Q1 = 1
nd.put_stub()

Tile_APD_length(0, Q1, i,j, True).put()



# Connection_Electrodes_Pads_Trapezoid(100,200,3,200,2).put()

# =============================================================================
# nd.strt(length  = 100000 , width = 0.1, layer = 1).put(-100000/2,0)
# nd.strt(width  = 100000 , length = 0.1, layer = 1).put(0,0)
# =============================================================================

# nd.strt(length  = 100000 , width = 0.1, layer = 1).put(-100000/2,0)
# nd.strt(width  = 100000 , length = 0.1, layer = 1).put(0,0)






nd.export_gds(filename=r'Device Tile')