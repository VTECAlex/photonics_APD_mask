### Beat note Detector Mask Design ###
### Date: 2024-07-25


import nazca as nd
import Reticle
import nazca.geometries as geom
from collections import defaultdict



nd.add_layer(name = "Designing Area for EBL", layer = 1)
nd.add_layer(name = "Waveguide", layer = 2)
nd.add_layer(name = "SiO Opening", layer = 3)
nd.add_layer(name = "P-Metallization", layer = 4)
nd.add_layer(name = "N-Metallization", layer = 5)
nd.add_layer(name = "Cutting Lanes", layer = 6)
nd.add_layer(name = "EBL AM", layer = 9)
nd.add_layer(name = "VTEC LOGO", layer = 8)
nd.add_layer(name = "P metal", layer = 9)
nd.add_layer(name = "Openings in SiO Inverted Function", layer = 10)
nd.add_layer(name = "Test_Layer", layer = 20)


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
def Layer_Difference(Remove_layer, From_layer, cell_name):
    pgons = merge_polygons(cell=cell_name, layers=[Remove_layer, From_layer])
    remove_polygons(cell=cell_name, layers=[Remove_layer, From_layer])  # optional
    pdiff = nd.clipper.diff_polygons(pgons[From_layer], pgons[Remove_layer])
    for pol in pdiff:
        nd.Polygon(points=pol, layer=From_layer).put(0)
    nd.netlist.pin2pin_drc_off()
    return cell_name












        ###############################################

##########Beggin_Frame
frame_L = 3800
frame_W = 3800
box = geom.frame(100, frame_L, frame_W)
nd.Polygon(box, layer="Designing Area for EBL").put()
###########End_Frame


with nd.Cell(name="Array_CTLMs") as Array_CTLM:
    outer_ring_r = 142
    gap_distance = 0
    gap_step = 5
    counter_goc = 0
    circle_reticle_layer = 'Metal Rings'
    goc = [8, 12, 16, 20, 25, 30, 35, 40, 50]
    for j in range(1, 4):
        for i in range(1, 4):
            with nd.Cell(name="CTLM{}".format(i)) as CTLM:
                middle_circle_r = 50
                cicrle_middle = nd.Polygon(layer="P metal",
                                           points=geom.circle(radius=middle_circle_r, N=700)).put(0, 0)
                gap_distance = gap_distance + gap_step
                inner_ring_r = middle_circle_r + goc[counter_goc]
                ring_width = outer_ring_r - inner_ring_r
                ring = nd.Polygon(layer="P metal",
                                  points=geom.ring(radius=outer_ring_r, width=ring_width, N=700)).put(0, 0)
                Frame = Reticle.ret(2 * inner_ring_r, 2 * inner_ring_r, outer_ring_r - inner_ring_r,
                                    "P metal")
                counter_goc = counter_goc + 1
            CTLM.put((outer_ring_r) * 2 * i, -(outer_ring_r) * 2 * j)
with nd.Cell("Group of CTLMS") as Group_CTLMS:
    Array_CTLM.put(-142, 3842)
    #Array_CTLM.put(-142 + 2848, 3842)
    Array_CTLM.put(-142 + 2848 - 1996 + 1144 / 2, 3842)


with nd.Cell ("SiO passivation") as SiO_passivation:
    nd.strt(length = 2400, width = 3700).put(0,3700/2)
SiO_passivation.put()

with nd.Cell("Squares Distance change") as squares_distance_change:
    size_box = 100
    for i in range(5):
        nd.strt(length = size_box,width = size_box, layer = "P metal").put(0,i*600)
        nd.strt(length = size_box,width = size_box, layer = "P metal").put((i+1)*200,i*600)

        # nd.strt(length = 200,width = 200, layer = "Openings in SiO Inverted Function").put(0,i*250)
        # nd.strt(length = 200,width = 200, layer = "Openings in SiO Inverted Function").put(i+250,i*250)
        #Layer_Difference("Openings in SiO Inverted Function", "SiO passivation", squares_distance_change)

squares_distance_change.put(2500,+650)


with nd.Cell("remove SiO boxes") as remove_SiO_boxes:

    nd.strt(length = )
    Layer_Difference("Openings in SiO Inverted Function", "SiO passivation", remove_SiO_boxes)



Group_CTLMS.put(0,0)
Group_CTLMS.put(0,-2848/2)
Group_CTLMS.put(0,-2848)

# Array_CTLM.put(-141,3842)
# Array_CTLM.put(-141,3842)
# Array_CTLM.put(-141,3842)



##DONT TOUCH THE POSITIONS OF THE AMS FOR EBL##
##DONT TOUCH THE POSITIONS OF THE AMS FOR EBL##
##DONT TOUCH THE POSITIONS OF THE AMS FOR EBL##
##DONT TOUCH THE POSITIONS OF THE AMS FOR EBL##
#############START EBL AM HERE#################
with nd.Cell(name = "Alignment mark") as am:
    size_of_box = 20
    for i in range(2):
        for j in range(2):
            nd.strt(width = size_of_box, length = size_of_box, layer = "EBL AM").put(300*i,300*j+10)
am.put(-800,-484)
am.put(800+3490,-484)
am.put(800+3490,484+3497)
am.put(-800,484+3497)
###############################################
##DONT TOUCH THE POSITIONS OF THE AMS FOR EBL##
##DONT TOUCH THE POSITIONS OF THE AMS FOR EBL##
##DONT TOUCH THE POSITIONS OF THE AMS FOR EBL##
##DONT TOUCH THE POSITIONS OF THE AMS FOR EBL##
##############END EBL AM HERE##################

nd.export_gds(filename='Metal_SC_test.gds')
