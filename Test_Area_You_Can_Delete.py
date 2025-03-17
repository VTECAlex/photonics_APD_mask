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
inner_length = sow * 2.54 * 10000+30+30+30 #Inner length +30 is to
inner_width = sow * 2.54 * 10000+30+30+30
diameter_of_wafer= sow * 2.54 * 10000
radius_of_wafer  = diameter_of_wafer/2
ring_width = 21000+15-30
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

nd.export_gds(filename=r'Test_Safe_For_delete')