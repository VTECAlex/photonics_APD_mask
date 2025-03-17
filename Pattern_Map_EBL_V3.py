### Beat note Detector Mask Design ###
### Date: 2024-07-25


import nazca as nd
import nazca.geometries as geo
import csv
from collections import defaultdict

def EBL_PatternMAp_V3(am_layer, frame_layer,frame_size, frame_clearance = True, show_pins =True):
    nd.add_layer(name = "Designing Area for EBL", layer = frame_layer)
    nd.add_layer(name = "EBL AM", layer = am_layer)
    with nd.Cell('EBL Map V3') as EBL_Map_V3:
        annotation_layer=34
        ##########Beggin_Frame
        with nd.Cell('Frame') as Frame:
            sizew = 100
            frame_L = 4000-sizew-20
            frame_W = 4000-sizew-20
            box = geo.frame(sizew, frame_L, frame_W)
            am_size = 20
            distance_am = 250
            am_map_size = frame_size
            if frame_clearance:
                nd.strt(length = sizew, width = am_map_size+am_size, layer=frame_layer).put(-am_map_size/2+2*distance_am+am_size/2,0)
                nd.Pin('Clear this area on the left').put(-am_map_size/2+2*distance_am+am_size/2,0)
                nd.strt(length = sizew, width = am_map_size+am_size, layer=frame_layer).put(am_map_size/2-2*distance_am+am_size/2-am_size-sizew,0)
                nd.Pin('Clear this area on the right').put(am_map_size/2-2*distance_am+am_size/2-am_size-sizew,0)
                if show_pins:
                    nd.put_stub()

        Frame.put(0,0)
        with nd.Cell('Am') as AM:
            coordinates = []
            am_size = 20
            distance_am = 500
            pinshow = False
            # am_map_size = 5000
            #Left Side
            for i in range(am_map_size//distance_am+1):
                nd.strt(length = am_size , width = am_size, layer = am_layer).put(-am_map_size/2-am_size/2,-am_map_size/2+i*distance_am)
                nd.Pin('{},{}'.format(-am_map_size/2,-am_map_size/2+i*distance_am)).put(-am_map_size/2,-am_map_size/2+i*distance_am)
                #nd.strt(length = am_size , width = am_size, layer = am_layer).put(-2500-am_size/2+distance_am,-2500+i*distance_am)
            for i in range(am_map_size//distance_am+1):
                nd.strt(length = am_size , width = am_size, layer = am_layer).put(am_map_size/2-am_size/2,-am_map_size/2+i*distance_am)
                nd.Pin('{},{}'.format(am_map_size/2,-am_map_size/2+i*distance_am)).put(am_map_size/2,-am_map_size/2+i*distance_am)
                #nd.strt(length = am_size , width = am_size, layer = am_layer).put(2500-am_size/2-distance_am,-2500+i*distance_am)

            for i in range(am_map_size // distance_am + 1):
                # Store coordinates for two points on the left side
                coordinates.append((-am_map_size/2 - am_size / 2, -am_map_size/2 + i * distance_am))
                coordinates.append((-am_map_size/2 - am_size / 2 + distance_am, -am_map_size/2 + i * distance_am))

            # Right Side
            for i in range(am_map_size // distance_am):
                # Store coordinates for two points on the right side
                coordinates.append((am_map_size/2 - am_size / 2, -am_map_size/2 + i * distance_am))
                coordinates.append((am_map_size/2 - am_size / 2 - distance_am, -am_map_size/2 + i * distance_am))

            with open('coordinates.csv', mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(['X Coordinate', 'Y Coordinate'])  # Header
                writer.writerows(coordinates)
            if show_pins:
                nd.put_stub()
        AM.put(0,0)
        nd.strt(length = frame_size , width =frame_size, layer = frame_layer+1000 ).put(-frame_size/2,0)
    return EBL_Map_V3

EBL_PatternMAp_V3(2,3,6000, False, True).put(0,0)

# def Cross_AM





nd.export_gds(filename='Pattern_MAP_EBL_Tile_V3.gds')
