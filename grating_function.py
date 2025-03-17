



import nazca as nd 
import math



def grating(width_size, pitch, num_grating = 100, length = 200, layer = 1, orientaion = 0):
    with nd.Cell(name = "Grating") as Grating:
        pos_x = 0
        pos_y = 0
        for num in range(num_grating):

            nd.strt(length = width_size, width = length, layer = layer).put(pos_x,pos_y)
            pos_x = pos_x + pitch
    Grating.put(0,0, orientaion)

grating(width_size=500,pitch=1000,num_grating=50,length = 350, layer = 3, orientaion= 45)

nd.export_gds(filename = "grating_test_delete.gds")
