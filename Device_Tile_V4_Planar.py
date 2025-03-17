####
"""
This is a new effort for a new tile, the previous one is very complicated and it
doesn't make any sense
"""

import nazca as nd
import Modulator_Full_Design
import Frame_for_tile
import Metal_Pads
import Signal_Pads
import Ground_Internal
import Etch_Ground_SiO_mask
import Ground_External
import nazca.geometries as geom
import metal_corners_APD
from collections import defaultdict
import math
# import metal_corners



def APD_Tile_V2(extra_length, Quadrant, i,j, show_name, show_frame):

    with nd.Cell(name = 'Device Cell V3') as Device_cell_V3:
        nd.add_layer(name='MESA etch', layer=1, accuracy=0.001)
        nd.add_layer(name='SiO', layer=2, accuracy=0.001)
        nd.add_layer(name='Metal Rings', layer=3, accuracy=0.001)
        nd.add_layer(name='Metal Ring Openings', layer=33, accuracy=0.001)
        nd.add_layer(name='N Metal', layer=5, accuracy=0.001)
        nd.add_layer(name='Au plating ', layer=6, accuracy=0.001)
        nd.add_layer(name='Open Corners', layer=23, accuracy=0.001)
        nd.add_layer(name='Slice_OpeningMetal_Ring_Lift_Off', layer=223, accuracy=0.001)
        nd.add_layer(name='Metal Patches', layer=555, accuracy=0.001)
        nd.add_layer(name='SiO Cover', layer=123, accuracy=0.001)
        nd.add_layer(name='lay22', layer=22, accuracy=0.001) # this is the layer to remove for the N-type contacts later

        frame_length = 2000+556.29393
        frame_width = 4900
        fram_cut_area = 100
        if show_frame:
            Frame_for_tile.frafrafra(frame_length, frame_width, fram_cut_area,'SiO').put(-935,-620)
            Frame_for_tile.frafrafra(frame_length, frame_width, fram_cut_area,'MESA etch').put(-935,-620)

        SiO_Layer = nd.strt(length = frame_length, width = frame_width  , layer = 'SiO').put(-935,1830)
        with nd.Cell (name = 'Right Side Devices') as Right_side_Devices:

            sbent_radius = 300
            sbent_angle = 45

            bond_pad_size = 200
            trapezoid_height = 100

            APD_x_position = [-245.32,-245.32,-245.32,-245.32,-245.32]#0-(50-17.5)+(50+17.532)+27,-20-(50-17.5)+(50-31.652),-70-(50-17.5)+(50-45.652),-120-(50-17.5)-10.352,-170-(50-17.5)-16.042]
            APD_distance = 750

            # APD_Signal_length = 1000
            APD_RF_length = [80+95.39,80+89.7,80+75,80+61,80+46+0.88]
            APD_RF_length = [0,0,0,0,0]

            RF_True = False
            angle = 80 # This value is associated to the angle of the N- metalization
            APD_y_position = 1050
            P_type_ring_width = 15
            P_type_ring_distance = -7.5
            extra_length_radius = 30 +P_type_ring_distance
            APD_radii = [80 + extra_length_radius, 100 + extra_length_radius, 150 + extra_length_radius,
                         200 + extra_length_radius, 250 + extra_length_radius]
            P_type_ring_SiO_opening_width = 10
            space_MESA_N_metal=10
            N_metal_width = 60
            P_metal_width = 50
            k=0


            #for radius in APD_radii:
            while k<len(APD_radii):
                APD_RF_length = [80 + 95.39, 80 + 89.7, 80 + 75, 80 + 61, 80 + 46 + 0.88]
                APD_Signal_length = [800+293.12-50,800+273.12-50,800+223.12,800+173.12-50,800+123.12-50]

                APD_Signal_length = APD_Signal_length[k]
                APD_RF_length = [0, 0, 0, 0, 0]
                with nd.Cell(name = "Devices") as Devices:

                    MESA = nd.Polygon(layer='MESA etch', points=geom.circle(radius=APD_radii[k], N=700)).put(0, 0)
                    MESA = nd.Polygon(layer=111, points=geom.ring(radius=APD_radii[k]+10, width = 10, N=700)).put(0, 0)

                    P_type_Ring = nd.Polygon(layer='Metal Rings', points=geom.ring(radius=APD_radii[k]+P_type_ring_distance, width=P_type_ring_width, N=700)).put(0, 0)
                    P_type_Ring_opening = nd.Polygon(layer='Metal Ring Openings', points=geom.ring(radius=APD_radii[k]+P_type_ring_distance - (P_type_ring_width-P_type_ring_SiO_opening_width)/2, width=P_type_ring_SiO_opening_width, N=700)).put(0, 0)
                    P_Au_Plating = nd.strt(length=APD_Signal_length-trapezoid_height-bond_pad_size, width=P_metal_width, layer='Au plating ').put(APD_radii[k] + P_type_ring_distance-P_type_ring_width+2.5,0)#put(APD_radii[k]-P_type_ring_width- (P_type_ring_width-P_type_ring_SiO_opening_width)/2+P_type_ring_distance,0)
                    trapezoid_connection = Trapezoid_Electric_Pads(trapezoid_height, P_metal_width, bond_pad_size,layer='Au plating ').put()
                    Bond_pad_Au = nd.strt(length = bond_pad_size, width = bond_pad_size , layer = 'Au plating ').put(trapezoid_connection.pin["Pin_Connection_Electrodes_Pads_right_side"])
                    Rf_Metalization(Au_plating = 'Au plating ', N_metal_opening= 'Metal Ring Openings', N_metalization = 'N Metal',  radius = APD_radii[k]+space_MESA_N_metal+N_metal_width/2, width = N_metal_width,
                                    length = 300, angle = angle, bond_pad_size = bond_pad_size, trapezoid_height = trapezoid_height, APD_RF_length= APD_RF_length[k], RF_True= RF_True, sbent_angle = sbent_angle,sbent_radius= sbent_radius).put((APD_radii[k]+space_MESA_N_metal+N_metal_width/2)*math.sin((2*math.pi*angle/360)/2),(APD_radii[k]+space_MESA_N_metal+N_metal_width/2)*math.cos((2*math.pi*angle/360)/2),(180 - angle) / 2)
                    APD_name = nd.text(text = "r{}".format(int(APD_radii[k]-extra_length_radius)), height= 200, layer = 'Metal Rings').put(APD_radii[k]-P_type_ring_width- (P_type_ring_width-P_type_ring_SiO_opening_width)/2+P_type_ring_distance+200-110-150+50+80,100+107+70-60-67-50)

                Devices.put(APD_x_position[k],k*APD_y_position)
                print(k*APD_y_position)
                # APD_y_position = APD_y_position + APD_distance+APD_radii[k-1]+APD_radii[k]
                k=k+1
        Right_side_Devices.put(0176.84773-50+556.29393+10.352-2.5, -270)



        with nd.Cell (name = 'Left_side_Devices') as Left_side_Devices:

            sbent_radius = 300
            sbent_angle = 45

            bond_pad_size = 200
            trapezoid_height = 100

            APD_x_position = [0-(50-17.5),-20-(50-17.5),-70-(50-17.5),-120-(50-17.5),-170-(50-17.5)]
            APD_x_position = [-245.32+200,-245.32+200,-245.32+200,-245.32+200,-245.32+200]
            APD_distance = 600
            # APD_Signal_length = 1000
            APD_RF_length = [80+95.39,80+89.7,80+75,80+61,80+46+0.88]
            APD_RF_length = [0,0,0,0,0]

            RF_True = False
            angle = 80 # This value is associated to the angle of the N- metalization
            APD_y_position = 1050
            P_type_ring_width = 15
            P_type_ring_distance = -7.5
            extra_length_radius = 30+P_type_ring_distance
            APD_radii = [10 + extra_length_radius, 20 + extra_length_radius, 30 + extra_length_radius,
                         40 + extra_length_radius, 50 + extra_length_radius]
            P_type_ring_SiO_opening_width = 10
            space_MESA_N_metal=10
            N_metal_width = 60
            P_metal_width = 10
            k=0


            #for radius in APD_radii:
            while k<len(APD_radii):
                APD_RF_length = [80 + 95.39, 80 + 89.7, 80 + 75, 80 + 61, 80 + 46 + 0.88]

                APD_Signal_length = [800+293.12-50-163.185-50,800+273.12-50-73.185-50-30-50,800+223.12-163.185-50,800+173.12-50-153.185-50+130-50,800+123.12-50-163.185-100+180]
                APD_Signal_length = APD_Signal_length[k]

                APD_RF_length = [0, 0, 0, 0, 0]
                with nd.Cell(name = "Devices") as Devices:

                    MESA = nd.Polygon(layer='MESA etch', points=geom.circle(radius=APD_radii[k], N=700)).put(0, 0)
                    MESA_planar= nd.Polygon(layer=111, points=geom.ring(radius=APD_radii[k]+10, width = 10, N=700)).put(0, 0)

                    P_type_Ring_opening = nd.Polygon(layer='Metal Ring Openings', points=geom.ring(radius=APD_radii[k]+P_type_ring_distance - (P_type_ring_width-P_type_ring_SiO_opening_width)/2, width=P_type_ring_SiO_opening_width, N=700)).put(0, 0)
                    P_type_Ring = nd.Polygon(layer='Metal Rings',
                                             points=geom.ring(radius=APD_radii[k] + P_type_ring_distance,
                                                              width=P_type_ring_width, N=700)).put(0, 0)
                    nd.Pin(name="P_type_Ring_Connection").put(-APD_radii[k], 0)

                    box_for_lift_off = nd.strt(length=P_type_ring_width*(3/2), width=10, layer='Slice_OpeningMetal_Ring_Lift_Off').put(-APD_radii[k]+(P_type_ring_width*(3/2)-P_type_ring_width)/2,0)
                    box_for_lift_off_cover = nd.strt(length=P_type_ring_width*(3/2), width=10, layer='SiO Cover').put(-APD_radii[k]+(P_type_ring_width*(3/2)-P_type_ring_width)/2,0)

                    P_Au_Plating = nd.strt(length=APD_Signal_length-trapezoid_height-bond_pad_size, width=P_metal_width, layer='Au plating ').put(APD_radii[k] + P_type_ring_distance-P_type_ring_width+2.5,0)
                    trapezoid_connection = Trapezoid_Electric_Pads(trapezoid_height, P_metal_width, bond_pad_size,layer='Au plating ').put()
                    Bond_pad_Au = nd.strt(length = bond_pad_size, width = bond_pad_size , layer = 'Au plating ').put(trapezoid_connection.pin["Pin_Connection_Electrodes_Pads_right_side"])
                    Rf_Metalization(Au_plating = 'Au plating ', N_metal_opening= 'Metal Ring Openings', N_metalization = 'N Metal',  radius = APD_radii[k]+space_MESA_N_metal+N_metal_width/2, width = N_metal_width,
                                    length = 300, angle = angle, bond_pad_size = bond_pad_size, trapezoid_height = trapezoid_height, APD_RF_length= APD_RF_length[k], RF_True= RF_True, sbent_angle = sbent_angle,sbent_radius= sbent_radius).put((APD_radii[k]+space_MESA_N_metal+N_metal_width/2)*math.sin((2*math.pi*angle/360)/2),(APD_radii[k]+space_MESA_N_metal+N_metal_width/2)*math.cos((2*math.pi*angle/360)/2),(180 - angle) / 2)
                    APD_name = nd.text(text = "r{}".format(int(APD_radii[k]-extra_length_radius)), height= 200, layer = 'Metal Rings').put(APD_radii[k]-P_type_ring_width- (P_type_ring_width-P_type_ring_SiO_opening_width)/2+P_type_ring_distance+200-110-150+352+50+(+50+80),-277+60+67+50,0, flip = True, flop = True)

                Devices.put(APD_x_position[k],k*APD_y_position-4*1050)
                # APD_y_position = APD_y_position + APD_distance+APD_radii[k-1]+APD_radii[k]
                k=k+1
        Left_side_Devices.put(-165.3854+50+25+2.5, -270, flop = True, flip= True)



        if show_name:
            VTEC_name = nd.text(text="VTEC", height= 200).put(-685+150+50+667-480-100, -100+90-600, 0)
            VTEC_Device_Name = nd.text(text="R{}C{}Q{}".format(Quadrant,i,j), height= 200).put(-685+150+50+667,100+ 1000+700-2500+90, 0)

        if show_name == True:
            top_left = metal_corners_APD.Metal_corners('Metal Rings').put(-1000 + 115-25, 4279.86 + 0.14, -90)
            top_left_hole = metal_corners_APD.Metal_corners_hole('Open Corners').put(-1000 + 115 + 200 - 50-200+10,
                                                                            4279.86 + 0.14 - 200+25-10, 0)

            top_right = metal_corners_APD.Metal_corners('Metal Rings').put(1000 + 65+556.294, +4230+25, 180)
            top_right_hole = metal_corners_APD.Metal_corners_hole('Open Corners').put(1000 + 65 - 200+556.294+25-10, +4230 - 150+200-10, -90)

            bot_right = metal_corners_APD.Metal_corners('Metal Rings').put(-1000 + 2015+556.294+25, -1000 + 430 - 50, 90)
            bot_right_hole = metal_corners_APD.Metal_corners_hole('Open Corners').put(-1000 + 2015 - 200 + 50+556.294+200-10,
                                                                             -1000 + 430 - 50 + 200-25+10, -180)

            bot_left = metal_corners_APD.Metal_corners('Metal Rings').put(-1000 + 65, 430 - 1000-25)
            bot_left_hole = metal_corners_APD.Metal_corners_hole('Open Corners').put(-1000 + 65 + 200-25+10, 430 - 1000 + 150-200+10, -270)


        Layer_Difference('Metal Ring Openings', 'SiO', Device_cell_V3)
        Layer_Difference('Open Corners', 'SiO', Device_cell_V3)
        Layer_Difference('Slice_OpeningMetal_Ring_Lift_Off', 'Metal Rings', Device_cell_V3)



    return Device_cell_V3

def Rf_Metalization(Au_plating, N_metal_opening,N_metalization, radius, width, length, angle,bond_pad_size, trapezoid_height,APD_RF_length,RF_True,  sbent_angle, sbent_radius):

    # bond_pad_size = 200


    with nd.Cell(name  = "RF metal rings") as Rf_metal_rings:
        if RF_True:
            layer = Au_plating
    #with nd.Cell(name="Rf Metal Rings Up") as Rf_metal_rings_up:
            N_contact_ring_top = nd.bend(angle=angle, radius=radius, width=width, offset=0,layer=layer).put(0, 0, 90)
            bend_rf_top = nd.bend(radius=radius, width=width, angle=-(angle - 90) - (180 - angle) / 2,layer=layer).put(N_contact_ring_top.pin["a0"], flip=True)
            nd.strt(length=APD_RF_length, width=width,layer=layer).put()
            bend_after_strt = nd.bend(angle=sbent_angle, radius=sbent_radius, width=width, offset=0,layer=layer).put()
            nd.bend(angle=sbent_angle, radius=sbent_radius, width=width, offset=0,layer=layer).put(bend_after_strt.pin["b0"], flip=True)
            trapezoid_connection = Trapezoid_Electric_Pads(trapezoid_height, width, bond_pad_size,layer=layer).put()
            nd.strt(length=bond_pad_size, width=bond_pad_size, layer=layer).put(
            trapezoid_connection.pin["Pin_Connection_Electrodes_Pads_right_side"])
            termination_Rf_ring = nd.bend(radius=radius, width=width, angle=180 - angle,layer=layer).put(N_contact_ring_top.pin["b0"])


            N_contact_ring_bot = nd.bend(angle=angle, radius=radius, width=width, offset=0,layer=layer).put(termination_Rf_ring.pin["b0"])
            bend_rf_top = nd.bend(radius=radius, width=width, angle=-(angle - 90) - (180 - angle) / 2,layer=layer).put(N_contact_ring_bot.pin["b0"], flip=False)
            strt_after_ring_rf = nd.strt(length=APD_RF_length,width=width, layer=layer).put()
            bend_after_strt = nd.bend(angle=sbent_angle, radius=sbent_radius,width=width, offset=0, layer=layer).put(strt_after_ring_rf.pin["b0"], flip=True)
            nd.bend(angle=sbent_angle, radius=sbent_radius, width=width,offset=0, layer=layer).put(bend_after_strt.pin["b0"])
            trapezoid_connection = Trapezoid_Electric_Pads(trapezoid_height, width,bond_pad_size, layer).put()
            nd.strt(length=bond_pad_size, width=bond_pad_size, layer=layer).put(
            trapezoid_connection.pin["Pin_Connection_Electrodes_Pads_right_side"])

            width = 0.8 * width
            layer_difference = N_metal_opening
            N_contact_ring_top = nd.bend(angle=angle, radius=radius, width=width, offset=0, layer=N_metal_opening).put(0, 0, 90)
            bend_rf_top = nd.bend(radius=radius, width=width, angle=-(angle - 90) - (180 - angle) / 2, layer=N_metal_opening).put(
                N_contact_ring_top.pin["a0"], flip=True)

            N_contact_ring_bot = nd.bend(angle=angle, radius=radius, width=width, offset=0, layer=N_metal_opening).put(
                termination_Rf_ring.pin["b0"])
            bend_rf_top = nd.bend(radius=radius, width=width, angle=-(angle - 90) - (180 - angle) / 2, layer=N_metal_opening).put(
                N_contact_ring_bot.pin["b0"], flip=False)
            termination_Rf_ring = nd.bend(radius=radius, width=width, angle=180 - angle, layer=N_metal_opening).put(
                N_contact_ring_top.pin["b0"])

            N_metal_opening = N_metalization
            layer_difference = N_metal_opening
            N_contact_ring_top = nd.bend(angle=angle, radius=radius, width=width, offset=0, layer=N_metal_opening).put(0, 0, 90)
            bend_rf_top = nd.bend(radius=radius, width=width, angle=-(angle - 90) - (180 - angle) / 2, layer=N_metal_opening).put(
                N_contact_ring_top.pin["a0"], flip=True)

            N_contact_ring_bot = nd.bend(angle=angle, radius=radius, width=width, offset=0, layer=N_metal_opening).put(
                termination_Rf_ring.pin["b0"])
            bend_rf_top = nd.bend(radius=radius, width=width, angle=-(angle - 90) - (180 - angle) / 2, layer=N_metal_opening).put(
                N_contact_ring_bot.pin["b0"], flip=False)
            termination_Rf_ring = nd.bend(radius=radius, width=width, angle=180 - angle, layer=N_metal_opening).put(
                N_contact_ring_top.pin["b0"])



    return Rf_metal_rings
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

def Layer_Difference(Remove_layer,From_layer,cell_name):

    pgons = merge_polygons(cell=cell_name, layers=[Remove_layer, From_layer])
    remove_polygons(cell=cell_name, layers=[Remove_layer, From_layer])  # optional
    pdiff = nd.clipper.diff_polygons(pgons[From_layer], pgons[Remove_layer])
    for pol in pdiff:
        nd.Polygon(points=pol, layer=From_layer).put(0)
    nd.netlist.pin2pin_drc_off()
    return cell_name


i = 1
j = 3
Q1 = 1
nd.put_stub()

APD_Tile_V2(0, Q1, i,j, True, True).put()

nd.export_gds(filename=r'Device Tile V3 For N Substrate')