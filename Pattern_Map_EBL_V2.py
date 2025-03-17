### Beat note Detector Mask Design ###
### Date: 2024-07-25


import nazca as nd
import nazca.geometries as geo
import csv
from collections import defaultdict

def EBL_Map_V2(am_layer, frame_layer):
    nd.add_layer(name = "Designing Area for EBL", layer = frame_layer)
    nd.add_layer(name = "EBL AM", layer = am_layer)
    with nd.Cell('EBL Map V2') as EBL_Map_V2:
        ##########Beggin_Frame
        with nd.Cell('Frame') as Frame:
            sizew = 100
            frame_L = 4000-sizew-20
            frame_W = 4000-sizew-20
            box = geo.frame(sizew, frame_L, frame_W)
            am_size = 20
            distance_am = 250
            am_map_size = 5000
            nd.strt(length = sizew, width = am_map_size+am_size, layer=frame_layer).put(-am_map_size/2+2*distance_am+am_size/2,0)
            nd.strt(length = sizew, width = am_map_size+am_size, layer=frame_layer).put(am_map_size/2-2*distance_am+am_size/2-am_size-sizew,0)
            nd.strt(length = am_map_size-4*distance_am-am_size, width = sizew, layer=frame_layer).put(-(am_map_size-4*distance_am-am_size)/2,2460)
            nd.strt(length = am_map_size-4*distance_am-am_size, width = sizew, layer=frame_layer).put(-(am_map_size-4*distance_am-am_size)/2,-2460)
        Frame.put(0,0)
        with nd.Cell('Am') as AM:
            coordinates = []
            am_size = 20
            distance_am = 500
            am_map_size = 5000
            #Left Side
            for i in range(am_map_size//distance_am+1):
                nd.strt(length = am_size , width = am_size, layer = am_layer).put(-2500-am_size/2,-2500+i*distance_am)
                nd.strt(length = am_size , width = am_size, layer = am_layer).put(-2500-am_size/2+distance_am,-2500+i*distance_am)
            for i in range(am_map_size//distance_am+1):
                nd.strt(length = am_size , width = am_size, layer = am_layer).put(2500-am_size/2,-2500+i*distance_am)
                nd.strt(length = am_size , width = am_size, layer = am_layer).put(2500-am_size/2-distance_am,-2500+i*distance_am)

            for i in range(am_map_size // distance_am + 1):
                # Store coordinates for two points on the left side
                coordinates.append((-2500 - am_size / 2, -2500 + i * distance_am))
                coordinates.append((-2500 - am_size / 2 + distance_am, -2500 + i * distance_am))

            # Right Side
            for i in range(am_map_size // distance_am):
                # Store coordinates for two points on the right side
                coordinates.append((2500 - am_size / 2, -2500 + i * distance_am))
                coordinates.append((2500 - am_size / 2 - distance_am, -2500 + i * distance_am))

            with open('coordinates.csv', mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(['X Coordinate', 'Y Coordinate'])  # Header
                writer.writerows(coordinates)
        AM.put(0,0)
    return EBL_Map_V2

EBL_Map_V2(2,3).put()
def List_Of_Coordinates_AM(am_size, distance_am, am_map_size):
    print('Left hand side coordinates:')
    for i in range(am_map_size//distance_am+1):
        print('x:{},y:{}'.format(-2500-am_size/2+10,-2500+i*distance_am))
    for i in range(am_map_size // distance_am+1):
        print('x:{},y:{}'.format(-2500-am_size/2+distance_am+10,-2500+i*distance_am))
    print('Right hand side coordinates:')
    for i in range(am_map_size // distance_am+1):
        print(':x:{},y:{}'.format(2500-am_size/2,-2500+i*distance_am))
    for i in range(am_map_size // distance_am+1):
        print(':x:{},y:{}'.format(2500-am_size/2-distance_am,-2500+i*distance_am))
am_size = 20
distance_am = 250
am_map_size = 5000
# List_Of_Coordinates_AM(am_size, distance_am, am_map_size)
# def Cross_AM





# nd.export_gds(filename='Pattern_MAP_EBL_Tile_V2.gds')
