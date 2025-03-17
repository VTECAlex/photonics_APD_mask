import nazca as nd
import nazca.geometries as geom
#import Reticle1
#import doted_circle

starting_length = 50
increasing_step = 0
number_of_grating = 50
grating_pitch = 2
grating_width = 1
with nd.Cell(name="grating") as grating:
    for i in range(number_of_grating+1):

        nd.strt(layer = 2, length = grating_width, width = starting_length+i*increasing_step).put(i*grating_pitch+grating_width,0)


grating.put(0,0)

nd.export_gds(filename="Grating_V1.gds")