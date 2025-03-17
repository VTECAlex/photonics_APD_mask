### Beat note Detector Mask Design ###
### Date: 2024-07-25


import nazca as nd
import nazca.geometries as geo
from BeatNoteDesign_Active_Layer_SOA import Lasers_Group
import csv
from collections import defaultdict




nd.add_layer(name ="Coarse and Fine" , layer = 2, accuracy = 0.001, overwrite=True)
nd.add_layer(name ="Pattern" , layer = 3, accuracy = 0.001, overwrite=True)
nd.add_layer(name ="Pre Alignment Mark" , layer = 4, accuracy = 0.001, overwrite=True)
nd.add_layer(name ="Frame Designing Area" , layer = 5, accuracy = 0.001, overwrite=True)
nd.add_layer(name ="Metal Corners" , layer = 6, accuracy = 0.001, overwrite=True)
nd.add_layer(name ="SOA MESA" , layer = 7, accuracy = 0.001, overwrite=True)
nd.add_layer(name ="SOA SiO Openings" , layer = 8, accuracy = 0.001, overwrite=True)
nd.add_layer(name ="p-Metallization" , layer = 9, accuracy = 0.001, overwrite=True)
nd.add_layer(name ="Cutting Lanes" , layer = 10, accuracy = 0.001, overwrite=True)
nd.add_layer(name ="VTEC Logo" , layer = 11, accuracy = 0.001, overwrite=True)
nd.add_layer(name ="Centered AM" , layer = 12, accuracy = 0.001, overwrite=True)
nd.add_layer(name ="Text Layer" , layer = 13, accuracy = 0.001, overwrite=True)
nd.add_layer(name ="n-Metallization" , layer = 14, accuracy = 0.001, overwrite=True)
nd.add_layer(name ="Ground SiO Opening" , layer = 16, accuracy = 0.001, overwrite=True)
nd.add_layer(name ="Ground Bottom SiO Opening" , layer = 17, accuracy = 0.001, overwrite=True)
nd.add_layer(name ="Pin Layer" , layer = 18, accuracy = 0.001, overwrite=True)
nd.add_layer(name ="Three Inch Wafer" , layer = 19, accuracy = 0.001, overwrite=True)


def EBL_PatternMAp_V3_Active_SOAs(am_layer,
                                  frame_layer,frame_size,
                                  frame_clearance = False,
                                  show_pins =True,
                                  posx = 0,
                                  posy = 0,
                                  Layer_MESA_SOA=1,
                                  Layer_SOA_SiO_Opening=1,
                                  Layer_P_Metallization =1,
                                  Layer_N_Metallization = 1,
                                  Layer_Ground_SiO_Opening =1,
                                  Layer_Ground_SiO_Opening_Bottom = 1,
                                  Layer_Cutting_Lanes = 1,
                                  Layer_Metal_Corner = 1,
                                  Pin_Layer = 1):

    with nd.Cell('EBL Map V3:{},{}'.format(posx,posy)) as EBL_Map_V3:
        ##########Beggin_Frame
        with nd.Cell('Frame:{},{}'.format(posx,posy)) as Frame:
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
                nd.put_stub()

        Frame.put(0,0)
        with nd.Cell('Am:{},{}'.format(posx,posy)) as AM:
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
            nd.put_stub()
        AM.put(0,0)
        Lasers_Group(12,
                     posx,
                     posy,
                     Layer_MESA_SOA,
                     Layer_SOA_SiO_Opening,
                     Layer_P_Metallization,
                     Layer_N_Metallization,
                     Layer_Ground_SiO_Opening,
                     Layer_Ground_SiO_Opening_Bottom,
                     Layer_Cutting_Lanes,
                     Layer_Metal_Corner,
                     Pin_Layer ).put(-2440+280/2,-1425-425)
        nd.strt(length = frame_size , width =frame_size, layer = frame_layer ).put(-frame_size/2,0)
    return EBL_Map_V3



EBL_PatternMAp_V3_Active_SOAs("Pattern",
                              "Frame Designing Area",
                              6000,
                              False,
                              True,
                              0,
                              0,
                              "SOA MESA",
                              "SOA SiO Openings",
                              "p-Metallization",
                              "n-Metallization",
                              "Ground SiO Opening",
                              "Ground Bottom SiO Opening",
                              "Cutting Lanes",
                              "Metal Corners",
                              "Pin Layer").put(0,0)
nd.export_gds(filename='Pattern_MAP_EBL_Tile_V3_Active_SOAs.gds')

