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
import metal_corners
from collections import defaultdict
import math
import metal_corners



def PCM_Dark_Current(extra_length, Quadrant, i,j, show_name, show_frame):

    with nd.Cell(name = 'Device Cell V2') as Dark_Current_PCM_V1:
        nd.add_layer(name='MESA etch', layer=1, accuracy=0.001)
        nd.add_layer(name='SiO', layer=2, accuracy=0.001)
        nd.add_layer(name='Metal Rings', layer=3, accuracy=0.001)
        nd.add_layer(name='Metal Ring Openings', layer=33, accuracy=0.001)
        nd.add_layer(name='N Metal', layer=5, accuracy=0.001)
        nd.add_layer(name='Au plating ', layer=6, accuracy=0.001)
        nd.add_layer(name='Open Corners', layer=23, accuracy=0.001)
        nd.add_layer(name='lay22', layer=22, accuracy=0.001) # this is the layer to remove for the N-type contacts later

        frame_length = 2000
        frame_width = 4900
        fram_cut_area = 100
        if show_frame:
            Frame_for_tile.frafrafra(frame_length, frame_width, fram_cut_area,'SiO').put(-935,-620)
            Frame_for_tile.frafrafra(frame_length, frame_width, fram_cut_area,'MESA etch').put(-935,-620)

        SiO_Layer = nd.strt(length = frame_length, width = frame_width  , layer = 'SiO').put(-935,1830)



        bond_pad_size = 200
        trapezoid_height = 100
        # APD_radii = [80, 100, 150, 200,250]
        # APD_x_position = [-40,-55.685,-80.385,-104.385,-128.505]
        P_type_ring_distance = -7.5
        extra_length_radius = 30 + P_type_ring_distance +7.5+40
        APD_radii = [80 + extra_length_radius-15, 100 + extra_length_radius -15, 150 + extra_length_radius-15,
                     200 + extra_length_radius-15, 250 + extra_length_radius-15]
        APD_x_position = [-56-11.5, -52.5-22.5-12.5, -117.2-7.8-12.5, -181.2+6.2-12.5, -245.32+20.32-12.5]
        APD_distance = 600
        APD_Signal_length = 1000
        APD_RF_length = [80+95.39,80+89.7,80+75,80+61,80+46+0.88]
        RF_True = False
        angle = 80 # This value is associated to the angle of the N- metalization
        APD_y_position = 1050

        P_type_ring_width = 25
        P_type_ring_distance = -30
        P_type_ring_SiO_opening_width = 15
        space_MESA_N_metal=5
        N_metal_width = 60
        P_metal_width = 50
        k=0


        #for radius in APD_radii:
        while k<len(APD_radii):
            with nd.Cell(name = "Devices") as Devices:

                MESA = nd.Polygon(layer='MESA etch', points=geom.circle(radius=APD_radii[k], N=700)).put(0, 0)
                P_type_Ring = nd.Polygon(layer='Metal Rings', points=geom.ring(radius=APD_radii[k]+P_type_ring_distance, width=P_type_ring_width, N=700)).put(0, 0)
                P_type_Ring_opening = nd.Polygon(layer='Metal Ring Openings', points=geom.ring(radius=APD_radii[k]+P_type_ring_distance - (P_type_ring_width-P_type_ring_SiO_opening_width)/2, width=P_type_ring_SiO_opening_width, N=700)).put(0, 0)
                P_Au_Plating = nd.strt(length=APD_Signal_length-trapezoid_height-bond_pad_size, width=P_metal_width, layer='Au plating ').put(APD_radii[k] + P_type_ring_distance-P_type_ring_width+2.5,0)
                trapezoid_connection = Trapezoid_Electric_Pads(trapezoid_height, P_metal_width, bond_pad_size,layer='Au plating ').put()
                Bond_pad_Au = nd.strt(length = bond_pad_size, width = bond_pad_size , layer = 'Au plating ').put(trapezoid_connection.pin["Pin_Connection_Electrodes_Pads_right_side"])
                Rf_Metalization(Au_plating = 'Au plating ', N_metal_opening= 'Metal Ring Openings', N_metalization = 'N Metal',  radius = APD_radii[k]+space_MESA_N_metal+N_metal_width/2, width = N_metal_width,
                                length = 300, angle = angle, bond_pad_size = bond_pad_size, trapezoid_height = trapezoid_height, APD_RF_length= APD_RF_length[k], RF_True= RF_True).put((APD_radii[k]+space_MESA_N_metal+N_metal_width/2)*math.sin((2*math.pi*angle/360)/2),(APD_radii[k]+space_MESA_N_metal+N_metal_width/2)*math.cos((2*math.pi*angle/360)/2),(180 - angle) / 2)
                APD_name = nd.text(text = "r{}".format(int(APD_radii[k]-extra_length_radius+15)), height= 200, layer = 'Metal Rings').put(APD_radii[k]-P_type_ring_width- (P_type_ring_width-P_type_ring_SiO_opening_width)/2+P_type_ring_distance+200-110-150+220,-127-50+100+107+70)#put(APD_radii[k]-P_type_ring_width- (P_type_ring_width-P_type_ring_SiO_opening_width)/2+P_type_ring_distance+200-110,100+107)

            Devices.put(APD_x_position[k],k*APD_y_position-270)
            # APD_y_position = APD_y_position + APD_distance+APD_radii[k-1]+APD_radii[k]
            k=k+1

            ######Metal Corners, checking if the TIle APD is part of the PCM or stand alone
            if True:

                # top_left  = metal_corners.Metal_corners('Metal Rings').put(-1000+115,4279.86+0.14,-90)
                # top_left_hole  = metal_corners.Metal_corners('Open Corners').put(-1000+115+200-50,4279.86+0.14-200,90)


                top_right  = metal_corners.Metal_corners('Metal Rings').put(1000+65,+4230+25,180)
                top_right_hole  = metal_corners.Metal_corners_hole('Open Corners').put(1000+65-200+25-10,+4230-150+200-10,-90)


                bot_right  = metal_corners.Metal_corners('Metal Rings').put(-1000+2015+25,-1000+430-50,90)
                bot_right_hole  = metal_corners.Metal_corners_hole('Open Corners').put(-1000+2015-200+50+200-10,-1000+430-50+200-25+10,180)


                # bot_left = metal_corners.Metal_corners('Metal Rings').put(-1000+65,430-1000)
                # bot_left_hole = metal_corners.Metal_corners('Open Corners').put(-1000+65+200,430-1000+150,180)
                Layer_Difference('Open Corners', 'SiO', Dark_Current_PCM_V1)




            Layer_Difference('Metal Ring Openings', 'SiO',Dark_Current_PCM_V1)

        if False:
            VTEC_name = nd.text(text="VTEC-LS", height= 400).put(-685+150+50, -100, 90)
            VTEC_Device_Name = nd.text(text="R{}C{}Q{}".format(Quadrant,i,j), height= 400).put(-685+150+50,100+ 1000+700, 90)


    return Dark_Current_PCM_V1






def PCM_Dark_Current_Planar(extra_length, Quadrant, i,j, show_name, show_frame):

    with nd.Cell(name = 'Device Cell V2') as Dark_Current_PCM_Planar:
        nd.add_layer(name='MESA etch', layer=1, accuracy=0.001)
        nd.add_layer(name='Planar Ring', layer=222, accuracy=0.001)
        nd.add_layer(name='SiO', layer=2, accuracy=0.001)
        nd.add_layer(name='Metal Rings', layer=3, accuracy=0.001)
        nd.add_layer(name='Metal Ring Openings', layer=33, accuracy=0.001)
        nd.add_layer(name='N Metal', layer=5, accuracy=0.001)
        nd.add_layer(name='Au plating ', layer=6, accuracy=0.001)
        nd.add_layer(name='Open Corners', layer=23, accuracy=0.001)
        nd.add_layer(name='lay22', layer=22, accuracy=0.001) # this is the layer to remove for the N-type contacts later

        frame_length = 2000
        frame_width = 4900
        fram_cut_area = 100
        if show_frame:
            Frame_for_tile.frafrafra(frame_length, frame_width, fram_cut_area,'SiO').put(-935,-620)
            Frame_for_tile.frafrafra(frame_length, frame_width, fram_cut_area,'MESA etch').put(-935,-620)

        SiO_Layer = nd.strt(length = frame_length, width = frame_width  , layer = 'SiO').put(-935,1830)



        bond_pad_size = 200
        trapezoid_height = 100
        # APD_radii = [80, 100, 150, 200,250]
        # APD_x_position = [-40,-55.685,-80.385,-104.385,-128.505]
        P_type_ring_distance = -7.5
        extra_length_radius = 30 + P_type_ring_distance +7.5+40
        APD_radii = [80 + extra_length_radius-15, 100 + extra_length_radius -15, 150 + extra_length_radius-15,
                     200 + extra_length_radius-15, 250 + extra_length_radius-15]
        APD_x_position = [-56-11.5, -52.5-22.5-12.5, -117.2-7.8-12.5, -181.2+6.2-12.5, -245.32+20.32-12.5]
        APD_distance = 600
        APD_Signal_length = 1000
        APD_RF_length = [80+95.39,80+89.7,80+75,80+61,80+46+0.88]
        RF_True = False
        angle = 80 # This value is associated to the angle of the N- metalization
        APD_y_position = 1050

        P_type_ring_width = 25
        P_type_ring_distance = -30
        P_type_ring_SiO_opening_width = 15
        space_MESA_N_metal=5
        N_metal_width = 60
        P_metal_width = 50
        k=0


        #for radius in APD_radii:
        while k<len(APD_radii):
            with nd.Cell(name = "Devices") as Devices:

                MESA = nd.Polygon(layer='MESA etch', points=geom.circle(radius=APD_radii[k], N=700)).put(0, 0)
                Planar = nd.Polygon(layer='Planar Ring', points=geom.ring(radius=APD_radii[k]+10, width = 10, N=700)).put(0, 0)
                P_type_Ring = nd.Polygon(layer='Metal Rings', points=geom.ring(radius=APD_radii[k]+P_type_ring_distance, width=P_type_ring_width, N=700)).put(0, 0)
                P_type_Ring_opening = nd.Polygon(layer='Metal Ring Openings', points=geom.ring(radius=APD_radii[k]+P_type_ring_distance - (P_type_ring_width-P_type_ring_SiO_opening_width)/2, width=P_type_ring_SiO_opening_width, N=700)).put(0, 0)
                P_Au_Plating = nd.strt(length=APD_Signal_length-trapezoid_height-bond_pad_size, width=P_metal_width, layer='Au plating ').put(APD_radii[k] + P_type_ring_distance-P_type_ring_width+2.5,0)
                trapezoid_connection = Trapezoid_Electric_Pads(trapezoid_height, P_metal_width, bond_pad_size,layer='Au plating ').put()
                Bond_pad_Au = nd.strt(length = bond_pad_size, width = bond_pad_size , layer = 'Au plating ').put(trapezoid_connection.pin["Pin_Connection_Electrodes_Pads_right_side"])
                Rf_Metalization(Au_plating = 'Au plating ', N_metal_opening= 'Metal Ring Openings', N_metalization = 'N Metal',  radius = APD_radii[k]+space_MESA_N_metal+N_metal_width/2, width = N_metal_width,
                                length = 300, angle = angle, bond_pad_size = bond_pad_size, trapezoid_height = trapezoid_height, APD_RF_length= APD_RF_length[k], RF_True= RF_True).put((APD_radii[k]+space_MESA_N_metal+N_metal_width/2)*math.sin((2*math.pi*angle/360)/2),(APD_radii[k]+space_MESA_N_metal+N_metal_width/2)*math.cos((2*math.pi*angle/360)/2),(180 - angle) / 2)
                APD_name = nd.text(text = "r{}".format(int(APD_radii[k]-extra_length_radius+15)), height= 200, layer = 'Metal Rings').put(APD_radii[k]-P_type_ring_width- (P_type_ring_width-P_type_ring_SiO_opening_width)/2+P_type_ring_distance+200-110-150+220,-127-50+100+107+70)#put(APD_radii[k]-P_type_ring_width- (P_type_ring_width-P_type_ring_SiO_opening_width)/2+P_type_ring_distance+200-110,100+107)

            Devices.put(APD_x_position[k],k*APD_y_position-270)
            # APD_y_position = APD_y_position + APD_distance+APD_radii[k-1]+APD_radii[k]
            k=k+1

            ######Metal Corners, checking if the TIle APD is part of the PCM or stand alone
            if True:

                # top_left  = metal_corners.Metal_corners('Metal Rings').put(-1000+115,4279.86+0.14,-90)
                # top_left_hole  = metal_corners.Metal_corners('Open Corners').put(-1000+115+200-50,4279.86+0.14-200,90)


                top_right  = metal_corners.Metal_corners('Metal Rings').put(1000+65,+4230+25,180)
                top_right_hole  = metal_corners.Metal_corners_hole('Open Corners').put(1000+65-200+25-10,+4230-150+200-10,-90)


                bot_right  = metal_corners.Metal_corners('Metal Rings').put(-1000+2015+25,-1000+430-50,90)
                bot_right_hole  = metal_corners.Metal_corners_hole('Open Corners').put(-1000+2015-200+50+200-10,-1000+430-50+200-25+10,180)


                # bot_left = metal_corners.Metal_corners('Metal Rings').put(-1000+65,430-1000)
                # bot_left_hole = metal_corners.Metal_corners('Open Corners').put(-1000+65+200,430-1000+150,180)
                Layer_Difference('Open Corners', 'SiO', Dark_Current_PCM_Planar)




            Layer_Difference('Metal Ring Openings', 'SiO',Dark_Current_PCM_Planar)

        if False:
            VTEC_name = nd.text(text="VTEC-LS", height= 400).put(-685+150+50, -100, 90)
            VTEC_Device_Name = nd.text(text="R{}C{}Q{}".format(Quadrant,i,j), height= 400).put(-685+150+50,100+ 1000+700, 90)


    return Dark_Current_PCM_Planar

def Rf_Metalization(Au_plating, N_metal_opening,N_metalization, radius, width, length, angle,bond_pad_size, trapezoid_height,APD_RF_length,RF_True):

    # bond_pad_size = 200
    sbent_radius = 300
    sbent_angle = 45

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


if __name__ == "__main__":
    i = 1
    j = 3
    Q1 = 1
    nd.put_stub()

    PCM_Dark_Current(0, Q1, i,j, True, True).put()
    PCM_Dark_Current_Planar(0, Q1, i,j, True, True).put(+3000,0)

    nd.export_gds(filename=r'Mask_GDS/Dark Current V3')