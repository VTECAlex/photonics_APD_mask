# -*- coding: utf-8 -*-
"""
Created on Tue Apr 11 12:49:48 2023

@author: alexa
Update of version 7
1) Change from 1-3 alignment to 2-3
2) Change from 1-4 alignment to 3-4


"""

import nazca as nd
import nazca.demofab as demo
import nazca.geometries as geom
import Tile
import Au_touch_plating_electrode

import Tile
import Device_Tile_V2
# import Tile_PCMs
import Device_Tile_V3_N_Sub
import Tile_PCMs_V2_N_Sub
import Reticle_Main
import doted_circle
import Ruler_at_the_bottom
from half_lean import leanSSS
from lean import leanS
from collections import defaultdict
import Tile_PCMs_V3_N_Sub
import lean


#import VTEC_logo



###### What is the size of the wafer (3 or 4 ''), what is the size of the reticle (usually 6'')
size_of_wafer = 3
size_of_reticle = 6
#################################
nd.add_layer(name='MESA etch', layer=1, accuracy=0.001)
nd.add_layer(name='MESA etch name', layer=11, accuracy=0.001)
nd.add_layer(name='SiO', layer=2, accuracy=0.001)
nd.add_layer(name='SiO name', layer=22, accuracy=0.001)
nd.add_layer(name='Metal Rings', layer=3, accuracy=0.001)
nd.add_layer(name='Metal Rings name', layer=334, accuracy=0.001)
nd.add_layer(name='Metal Ring Openings', layer=33, accuracy=0.001)
nd.add_layer(name='N Metal', layer=5, accuracy=0.001)
nd.add_layer(name='N Metal name', layer=55, accuracy=0.001)
nd.add_layer(name='Au plating ', layer=6, accuracy=0.001)
nd.add_layer(name='Au plating name', layer=66, accuracy=0.001)
nd.add_layer(name='Open Corners', layer=23, accuracy=0.001)
nd.add_layer(name='lay22', layer=22, accuracy=0.001)  # this is the layer to remove for the N-type contacts later


circle_reticle_layer = 65
logo_text_height = 3000
correction_placement = +300 #Correction on when the Logo is placed
sow = size_of_wafer
sor = size_of_reticle
outer_length = sor * 2.54 * 10000
outer_width = sor * 2.54 * 10000
inner_length = sow * 2.54 * 10000+30+60 #Inner length +30 is to
inner_width = sow * 2.54 * 10000+30+60
diameter_of_wafer= sow * 2.54 * 10000
radius_of_wafer  = diameter_of_wafer/2
ring_width = 21000+15
for layer in range(1,5):
    layer_names = ['MESA etch', 'SiO', 'Metal Rings', 'Metal Ring Openings', 'N Metal', 'Au plating ']
    ######Ring of the reticle
    wafer = nd.Polygon(layer=layer_names[layer-1], points=geom.ring(radius=inner_length / 2 + ring_width+30+30, width= ring_width+30, N=700)).put(0, 0)
    ######Reticle of the full mask
    Reticle_Main.ret(outer_length, outer_width, inner_length, inner_width, layer_names[layer-1])
    ######Dotted circle
    doted_circle.dotted_circle(layer_names[layer-1], size_of_wafer).put(0, 0)
    ######Top boxes reticle
    # nd.strt(length=6 * 2.54 * 10000, width=logo_text_height + 2 * correction_placement + 10000, layer=layer).put(
    #     -6 * 2.54 * 10000 / 2, (3 * 2.54 * 10000 - logo_text_height / 2) - correction_placement - 5000)
    ######Bottom boxes
    nd.strt(length=23110, width=2500, layer=layer_names[layer-1]).put(-11555, -50844.62)



##################### These are the leans 
def Leans_Vertical_and_Horizontal_funct(layer_leans,size_of_wafer):
    layer_names = ['MESA etch', 'SiO', 'Metal Rings', 'Metal Ring Openings', 'N Metal', 'Au plating ', 'lay22']
    layer_leans = layer_names[layer_leans]
    with nd.Cell(name = "Leans Vertical and Horixonatal") as Leans_Vertical_and_Horizontal:
        with nd.Cell(name = "DottedLines") as DottedLinesHor:
            dotted_length = 70
            dotted_width = 10
            for i in range(0, int((76.2*1000/4)//dotted_length)):
                nd.strt(length = dotted_length, width = dotted_width, layer = layer_leans).put(0,0)
                nd.strt(length = dotted_length, width = dotted_width, layer = layer_leans).put(-i*2*dotted_length ,0)
                nd.strt(length = dotted_length, width = dotted_width, layer = layer_leans).put(i*2*dotted_length,0)
        
        dotted_lane_width = 0
        DottedLinesHor.put(-35,0)
        #DottedLinesHor.put(0,dotted_lane_width/2+dotted_width)
        DottedLinesHor.put(0,-35,90)
        #DottedLinesHor.put(dotted_lane_width/2+dotted_width,0,90)
        
        
        
        
        #leanS.put(0,0)
        leanS_pitch = 1500
        leanS_range = 76
        excluded_leans = [ 0 ,1 ]
        for i in range(0,leanS_range):
            distance_of_number_from_lineals = 500
            size_of_number_of_lineals = 400
            sonol = size_of_number_of_lineals
            donfl = distance_of_number_from_lineals
            if i!=0:
                if i<(leanS_range-5)//2:
                    #These are the vertical ones
                    if size_of_wafer ==3:
                        range_for_bottom_ruler_is = 24
                    else:
                        range_for_bottom_ruler_is =  32
                    if i<range_for_bottom_ruler_is:
                        leanS(layer_leans).put(0,(-i)*leanS_pitch,90)
                    leanS(layer_leans).put(0,(+i-1)*leanS_pitch,90)
                    nd.text("{}".format(0),height= sonol, layer = layer_leans).put(500+380,-(0)*leanS_pitch-donfl)
                    nd.text("{}".format(0),height= sonol, layer = layer_leans).put(-500-360 - sonol,-0*leanS_pitch - donfl)
        
                    if size_of_wafer == 3:
                        range_for_bottom_ruler_is =24
                    else:
                        range_for_bottom_ruler_is = 32
                    if i<range_for_bottom_ruler_is:
                        extra_dist_negs = 0
                        nnew_dist = 0
                        if i>=10:
                            nnew_dist = 4
                        if i >=10:
                            extra_dist_negs = 244
                        nd.text("{}".format(-i),height= sonol, layer = layer_leans).put(500 +370- extra_dist_negs -10+nnew_dist,-(i)*leanS_pitch-donfl +85)
                        nd.text("{}".format(-i),height= sonol, layer = layer_leans).put(-500-360 - sonol,-i*leanS_pitch - donfl +85)
                    if i<=33:
                        extra_dist = 0 
                        if i < 10:
                            extra_dist = 244
                            
                        nd.text("{}".format(i),height= sonol, layer = layer_leans).put(500+330 +extra_dist -10,+i*leanS_pitch -donfl +85)
                        nd.text("{}".format(i),height= sonol, layer = layer_leans).put(-500 -373- sonol+13,+i*leanS_pitch -donfl+85)
        
        
                    #These are the horizonatal ones
                    if i !=1 and i!=0 and i!=2:
                        leanS(layer_leans).put((-i+1)*leanS_pitch,0)
                        leanS(layer_leans).put((i-1)*leanS_pitch,0)
                        if i<35:
                            extra_right_negs = 0
                            trololo = 0
                            if i<=10:
                                trololo = 30
                            if i > 10:
                                extra_right_negs = 210
                            nd.text("{}".format(-i+1),height= sonol, layer = layer_leans).put((-i+1)*leanS_pitch-800+355 - extra_right_negs + trololo,-donfl-sonol -454+9+5)
                            nd.text("{}".format(-i+1),height= sonol, layer = layer_leans).put((-i+1)*leanS_pitch-800+355-extra_right_negs + trololo ,donfl +373-8-5)
                    if i !=1 and i!=0:
                        if i<34:
                            extra_right =0
                            extra_two = 0
                            if i>9:
                                extra_two = 2
                            if i<10:
                                extra_right = 118
                            nd.text("{0:2}".format(i),height= sonol, layer = layer_leans).put(i*leanS_pitch-800+355+ extra_right-8 -extra_two ,-donfl-sonol -454+9+5)
                            nd.text("{0:2}".format(i),height= sonol, layer = layer_leans).put(i*leanS_pitch-800+355 + extra_right -8 -extra_two,donfl + 373-8-5)
    return Leans_Vertical_and_Horizontal
for i in range(6):
    Leans_Vertical_and_Horizontal_funct(i, size_of_wafer).put(0,0)



################ This is the vertical bottom RULER
with nd.Cell(name = "Bottom Vertical Ruler For Major Flat") as BVRFMF:
    leanS_pitch = 1500
    leanS_range = 80
    leanS_pitch_half = 1500

    leanS_range_half = 63
    Layer_ruler = 'MESA etch'
    excluded_leans_half = [ 0 ,1 ]
    for i in range(0,leanS_range_half-51):
        distance_of_number_from_lineals = 500
        size_of_number_of_lineals = 400
        sonol = size_of_number_of_lineals
        donfl = distance_of_number_from_lineals
        if i!=0:
                #These are the horizonatal ones
                if True:
                    leanSSS.put((-i+1)*leanS_pitch_half,-35000+400 -1842.527 -20)
                    leanSSS.put((i-1)*leanS_pitch_half,-35000+400 -1842.527 -20)
                    if i<12:
                        extra_right_negs = 0
                        if i > 10:
                            extra_right_negs = 210
                        nd.text("{}".format(-i+1),height= sonol, layer = Layer_ruler).put((-i+1)*leanS_pitch-800+355 - extra_right_negs,-donfl-sonol -454+9+5 -35000+400-1842.527 -20)
                        nd.text("{}".format(-i+1),height= sonol, layer = Layer_ruler).put((-i+1)*leanS_pitch_half-800+355-extra_right_negs,donfl +373-8-5 -35000+400-1842.527 -20)
                if True :
                    if i<11:
                        extra_right =0
                        if i<10:
                            extra_right = 118
                        if i<9:
                            nd.text("{0:2}".format(i),height= sonol, layer = Layer_ruler).put(i*leanS_pitch-800+355+ extra_right ,-donfl-sonol -454+9+5 -35000+400-1842.527-20)
                            nd.text("{0:2}".format(i),height= sonol, layer = Layer_ruler).put(i*leanS_pitch_half-800+355 + extra_right ,donfl + 373-8-5 -35000+400-1842.527-20)
                        else:
                            nd.text("{0:2}".format(i), height=sonol, layer=Layer_ruler).put(
                                i * leanS_pitch - 800 + 355 + extra_right,
                                -donfl - sonol - 454 + 9 + 5 - 35000 + 400 - 1842.527 - 20)
                            nd.text("{0:2}".format(i), height=sonol, layer=Layer_ruler).put(
                                i * leanS_pitch_half - 800 + 355 + extra_right,
                                donfl + 373 - 8 - 5 - 35000 + 400 - 1842.527 - 20)
fix_for_three_inch = 0
if size_of_wafer == 3:
    fix_for_three_inch = 11643.31+15-5
BVRFMF.put(0,-13117.093+1372.448+45+15+fix_for_three_inch)

######## Initial variation, the first tile, don't touch

tile_full_length_x_dir = 2100+(2756.294-2100)
tile_full_length_y_dir = 4900
pos1x_Q1 = tile_full_length_x_dir/2+1250+30
pos1y_Q1 = tile_full_length_y_dir/2+50+1250+30+50
step_x = tile_full_length_x_dir
step_y = tile_full_length_y_dir
        
emtpy_list = []

Total_per_Quadrant = 0

length_variation = [0,200,500,800,1000,0,200,500,800,1000,0,200,500,800,1000,0,200]



########For the PCM tile
tile_full_length_x_dir_PCM = 6900+380+1050
tile_full_length_y_dir_PCM = 4800
pos1x_Q1_PCM = tile_full_length_x_dir_PCM/2+50+1250+30-2580/2-500-525
pos1y_Q1_PCM = tile_full_length_y_dir_PCM/2+1250+30
step_x = tile_full_length_x_dir_PCM
step_y = tile_full_length_y_dir_PCM+200
        
###########################################################


for j in range(10):
    previous_position_for_Q_1_4 = pos1x_Q1 # previous positions for 1 and 4 quadrants Tile
    previous_position_for_Q_2_3 = pos1x_Q1-100 # previous positions for 2 and 3 quadrants Tile
    x_directio_length_of_all_tiles = 3350 # This is the starting position of the bottom right corner of the center of the tile
    previous_position_for_Q_1_4_PCM = pos1x_Q1_PCM # previous positions for 1 and 4 quadrants PCM
    previous_position_for_Q_2_3_PCM = pos1x_Q1_PCM # previous positions for 2 and 3 quadrants PCM
    x_directio_length_of_all_tiles_PCM = 0
    for i in range(17):
        extra_length =0
        x_directio_length_of_all_tiles  = x_directio_length_of_all_tiles + (tile_full_length_x_dir + extra_length ) 
        y_directio_length_of_all_tiles  = (j+1)*(tile_full_length_y_dir)
        x_directio_length_of_all_tiles_PCM  = x_directio_length_of_all_tiles_PCM + (tile_full_length_x_dir_PCM + extra_length )
        if (x_directio_length_of_all_tiles)**2+(y_directio_length_of_all_tiles)**2< (radius_of_wafer)**2: #This is x^2+y^2<r^2 so we have devices insied the r=4''/2
            Q1 = 1
            Q2 = 2
            Q3 = 3
            Q4 = 4
            if j!=3:
                Device_Tile_V3_N_Sub.APD_Tile_V2(extra_length, Q1, i, j, True, True).put(previous_position_for_Q_1_4 + extra_length/2 -15-328.147, pos1y_Q1 + j*step_y -1830 )
                Device_Tile_V3_N_Sub.APD_Tile_V2(extra_length, Q2, i, j, True, True).put(-previous_position_for_Q_2_3 - extra_length / 2 - 100 - 15 - 328.147, pos1y_Q1 + j * step_y - 1830)
                if size_of_wafer==4:
                    if j<9:
                        Device_Tile_V3_N_Sub.APD_Tile_V2(extra_length, Q4, i, j, True, True).put(previous_position_for_Q_1_4 + extra_length/2 -15-328.147, -pos1y_Q1 - j*step_y - 1830)
                        Device_Tile_V3_N_Sub.APD_Tile_V2(extra_length, Q3, i, j, True, True).put(-previous_position_for_Q_2_3  - extra_length/2 -100 -15-328.147, -pos1y_Q1 - j*step_y - 1830)
                else:
                    if j < 6:
                        Device_Tile_V3_N_Sub.APD_Tile_V2(extra_length, Q4, i, j, True, True).put(
                            previous_position_for_Q_1_4 + extra_length / 2 - 15 - 328.147, -pos1y_Q1 - j * step_y - 1830)
                        Device_Tile_V3_N_Sub.APD_Tile_V2(extra_length, Q3, i, j, True, True).put(
                            -previous_position_for_Q_2_3 - extra_length / 2 - 100 - 15 - 328.147,
                            -pos1y_Q1 - j * step_y - 1830)
                previous_position_for_Q_1_4 = previous_position_for_Q_1_4 + tile_full_length_x_dir-100
                previous_position_for_Q_2_3 = previous_position_for_Q_2_3 + tile_full_length_x_dir-100
        if (x_directio_length_of_all_tiles_PCM)**2+(y_directio_length_of_all_tiles)**2< (radius_of_wafer)**2:
            Q1 = 1
            Q2 = 4
            Q3 = 2
            Q4 = 3
            if j==3:
                Tile_PCMs_V3_N_Sub.Tile_PCMs_all(extra_length, Q1, i, j).put( previous_position_for_Q_1_4_PCM , pos1y_Q1 + j*step_y )
                Tile_PCMs_V3_N_Sub.Tile_PCMs_all(extra_length, Q2, i, j).put( previous_position_for_Q_1_4_PCM, -pos1y_Q1 - j*step_y )
                Tile_PCMs_V3_N_Sub.Tile_PCMs_all(extra_length, Q3, i, j).put( -previous_position_for_Q_1_4_PCM -2580+480-1000-1050, pos1y_Q1 + j*step_y )
                Tile_PCMs_V3_N_Sub.Tile_PCMs_all(extra_length, Q4, i, j).put( -previous_position_for_Q_1_4_PCM -2580+480-1000-1050,- pos1y_Q1 - j*step_y )
                previous_position_for_Q_1_4_PCM = previous_position_for_Q_1_4_PCM + tile_full_length_x_dir_PCM - 480
                previous_position_for_Q_2_3_PCM = previous_position_for_Q_2_3_PCM + tile_full_length_x_dir_PCM+100


        Total_per_Quadrant  = Total_per_Quadrant +1
#SiO covers for the rulers 
nd.strt(length =75350 + 12655*2, width =2520+40 , layer =2 ).put(-75350/2+175-12655,0)
nd.strt(width =75350+155-2472.4+ 12655*2, length =2520+20+20 , layer =2 ).put(-2520/2-10-10,155/2+2482.4-2472.4/2-462.02)
nd.strt(length = 23110-2*555+1110+2*4698 , width  = 2500-(2500-1285)+147.448, layer = 2).put(-4698-23110/2,147.448/2 - 40000+455.68+1816.793+2500-(2500-1285)/2-13117.093)
#nd.strt(length = 23110-2*555+1110+2*4698 , width  = 2500-(2500-1285)+147.448, layer = 1).put(-4698-23110/2,147.448/2 - 40000+455.68+1816.793+2500-(2500-1285)/2-13117.093)



############Touch electrode for the plating process 
Au_touch_plating_electrode.touch_electrode('Au plating ',size_of_wafer).put(0,0)


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

with nd.Cell(name = "Mask Names") as mask_names:
    ######Layer Mask Names
    Layer_MESA = nd.text("APD V2 Layer 1 MESA etching", height= 6000, layer= 'MESA etch name').put(-40000,-72510)


    # Layer_Difference('MESA etch name', 'MESA etch', mask_names)


    Layer_MESA = nd.text("APD V2 Layer 2 SiO openings", height= 6000, layer= 'SiO name' ).put(-40000,-72510)
    Layer_MESA = nd.text("APD V2 Layer 3 TiPtAu Ring", height= 6000, layer= 'Metal Rings name').put(-40000,-72510)
    Layer_MESA = nd.text("APD V2 Layer 4 Au Bond Pad", height= 6000, layer= 'Au plating name').put(-40000,-72510)
mask_names.put()


############ center line
# =============================================================================
# nd.strt(length  = 500000 , width = 0.1, layer = 1).put(-100000/2,0)
# nd.strt(width  = 500000 , length = 0.1, layer = 1).put(0,0)
# =============================================================================
print("The X direction", )
print(Total_per_Quadrant, 'Total number of tiles')






nd.export_gds(filename=r'APD {}'' Mask All layers N Sub'.format(size_of_wafer))




