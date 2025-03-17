### Beat note Detector Mask Design ###
### Date: 2024-07-25


import nazca as nd
import nazca.geometries as geo
from VTEC_logo import *
import metal_corners

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




def Lasers(gap, length,
           num_of_devices,posx=0
           ,posy=0,
           Layer_MESA_SOA=1,
           Layer_SOA_SiO_Opening=1,
           Layer_P_Metallization =1,
           Layer_N_Metallization = 1,
           Layer_Ground_SiO_Opening =1,
           Layer_Ground_SiO_Opening_Bottom = 1,
           Layer_Cutting_Lanes = 1,
           Layer_Metal_Corner = 1 ,
           Pin_Layer = 1 ):

    with nd.Cell(name="Lasers length:{},{},{}".format(length,posx,posy)) as Lasers_Length:
        additional_wvg_cutting_lane = 25
        additional_wvg_cutting_lane_metal = 0 # it used to be 20
        ground_metal_width = 100
        distance_between_SOAs = gap
        ground_metal_line_width = 70
        ground_metal_line_length = 40
        SOA_metallization_width = 100
        other_side_metallization = 4
        distance_SOAmetal_GROUNDmetal = 25
        extra_metal_on_cutting_lane_length  = 50/2 #this is the cutting lane length divided by 2
        extra_metal_on_cutting_lane_width  = 10

        gmw = ground_metal_width
        awcl = additional_wvg_cutting_lane
        awclm = additional_wvg_cutting_lane_metal
        gmlw = ground_metal_line_width
        gmll = ground_metal_line_length
        dsg = distance_SOAmetal_GROUNDmetal
        osm = other_side_metallization
        Smw = SOA_metallization_width
        emocll = extra_metal_on_cutting_lane_length
        emoclw  = extra_metal_on_cutting_lane_width
        SOA_width = []
        k = 0
        for i in range(num_of_devices):
            if 1.5 + k * 0.25 <= 2.5:
                SOA_width.append(1.5 + k * 0.25)
                k = k + 1
            else:
                k = 0
                SOA_width.append(1.5 + k * 0.25)
                k = k + 1
        for i in range(num_of_devices):
            text_linewidth =25
            with nd.Cell(name="Laser:{},{},{},{}".format(posx,posy,i,length)) as Laser:
                metallization_len = length
                ground_x_dir = 0
                ground_y_dir = -gmw / 2-SOA_width[i]/2-osm-dsg
                text1_x = +20 #metallization_len/7
                text1_y = Smw+15
                wvg_len = metallization_len+2*awcl

                wvg = nd.strt(length = wvg_len, width = SOA_width[i], layer =Layer_MESA_SOA).put(metallization_len-wvg_len+awcl,0)
                extra_waveguide_start = nd.strt(length=25, width=SOA_width[i], layer=Layer_MESA_SOA).put(wvg.pin["a0"])
                extra_waveguide_end = nd.strt(length=25, width=SOA_width[i], layer=Layer_MESA_SOA).put(wvg.pin["b0"])


                SiO_Openings = nd.strt(length=metallization_len + 2*emocll, width=SOA_width[i] * 0.75, layer=Layer_SOA_SiO_Opening).put(-awclm,0)
                SiO_Openings_for_the_start = nd.strt(length=50, width=SOA_width[i] * 0.75, layer=Layer_SOA_SiO_Opening).put(wvg.pin["a0"].move(-25,0))
                SiO_Openings_for_the_end = nd.strt(length=metallization_len + 2*emocll, width=SOA_width[i] * 0.75, layer=Layer_SOA_SiO_Opening).put(-awclm,0)

                Metallization = nd.strt(length=metallization_len + 2*awclm, width=Smw, layer=Layer_P_Metallization).put(-awclm, +Smw / 2 - SOA_width[i] / 2-osm)
                Metallization_extra_piece = nd.strt(length=2*emocll , width=emoclw, layer=Layer_P_Metallization).put(Metallization.pin["b0"].move(0,-45))
                Metallization_extra_start = nd.strt(length=2*emocll , width=emoclw, layer=Layer_P_Metallization).put(Metallization.pin["a0"].move(0,45))


                ground_metal = nd.strt(length=metallization_len, width=gmw, layer=Layer_N_Metallization).put(ground_x_dir, ground_y_dir)
                ground_sio_open = nd.strt(length=metallization_len - 10, width=gmw-10, layer=Layer_Ground_SiO_Opening).put(+ground_x_dir+5,ground_y_dir)
                ground_sio_bottom_open = nd.strt(length=metallization_len - 10 - 10, width=gmw -20, layer=Layer_Ground_SiO_Opening_Bottom).put(ground_x_dir+10,ground_y_dir)




                nd.text("SOA W:{} L:{}".format(SOA_width[i],length, awclm), height =text_linewidth, layer=Layer_P_Metallization).put(text1_x,text1_y)


            Laser.put(0, (i + 1) * distance_between_SOAs - 130 - 190 / 2 + 62.75+170/2-(+93-37.25)/2)
            cutting_lane_1 = nd.strt(length=50, width=3800, layer=Layer_Cutting_Lanes).put(-50, 3700 / 2)
            # metal_corners_layer = 47
            #These are the metal corners on the left side of each column of laser
            metal_corners_layer = Layer_Metal_Corner
            metal_corners.Metal_corners(metal_corners_layer,length,1,posx,posy,i).put(0,3775)
            metal_corners.Metal_corners(metal_corners_layer,length,2,posx,posy,i).put(0,-75,flip = True)
            metal_corners.Metal_corners(metal_corners_layer,length,3,posx,posy,i).put(-50,3775, flop=True)
            metal_corners.Metal_corners(metal_corners_layer,length,4,posx,posy,i).put(-50,-75, flop=True, flip=True)
            cutting_lane_1_5 = nd.strt(length=50, width=3800, layer=Layer_Cutting_Lanes).put(length, 3700 / 2)
            #These are the metal corners on the right side of each column of laser
            metal_corners.Metal_corners(metal_corners_layer,length,5,posx,posy,i).put(length+50,3775)
            metal_corners.Metal_corners(metal_corners_layer,length,6,posx,posy,i).put(length+50,-75,flip = True)
            metal_corners.Metal_corners(metal_corners_layer,length,7,posx,posy,i).put(-50+length+50,3775, flop=True)
            metal_corners.Metal_corners(metal_corners_layer,length,8,posx,posy,i).put(-50+length+50,-75, flop=True, flip=True)
        return Lasers_Length

def Lasers_Group(num_of_devices_each_column,
                 posx,
                 posy,
                 Layer_MESA_SOA=1,
                 Layer_SOA_SiO_Opening=1,
                 Layer_P_Metallization =1,
                 Layer_N_Metallization = 1,
                 Layer_Ground_SiO_Opening =1,
                 Layer_Ground_SiO_Opening_Bottom = 1,
                 Layer_Cutting_Lanes = 1,
                 Layer_Metal_Corner = 1 ,
                 Pin_Layer = 1):

    with nd.Cell('Lasers Group:{},{}'.format(posx,posy)) as Lasers_group:
        Lasers_length = [250,400, 500,600,750,800,1000]
        cutting_lane_length = 50
        x = 0
        # num_of_devices_each_column = 12
        for laser_len in Lasers_length:
            Lasers(300,
                   laser_len,
                   num_of_devices_each_column,
                   posx, posy,Layer_MESA_SOA,
                   Layer_SOA_SiO_Opening,
                   Layer_P_Metallization,
                   Layer_N_Metallization,
                   Layer_Ground_SiO_Opening,
                   Layer_Ground_SiO_Opening_Bottom,
                   Layer_Cutting_Lanes,
                   Layer_Metal_Corner,
                   Pin_Layer).put(x + Lasers_length.index(laser_len)*cutting_lane_length,0)
            x = x + laser_len
        cutting_lane_width = 50
        cutting_lanes_length = x+int(len(Lasers_length))*cutting_lane_width
        cutting_lane_bottom = nd.strt(length = cutting_lane_width, width =cutting_lanes_length,layer = Layer_Cutting_Lanes).put(cutting_lanes_length/2,-cutting_lane_width,90)
        cutting_lane_top = nd.strt(length = cutting_lane_width, width =cutting_lanes_length,layer = Layer_Cutting_Lanes).put(cutting_lanes_length/2,3700,90)
    return Lasers_group


Lasers_Group(12,0,0,"SOA MESA",
             "SOA SiO Openings",
             "p-Metallization",
             "n-Metallization",
             "Ground SiO Opening",
             "Ground Bottom SiO Opening",
             "Cutting Lanes",
             "Metal Corners",
             "Pin Layer").put(0,0)
# VTEC_Logo("VTEC_logo",0,0).put(0,0)
nd.export_gds(filename='Beatnote_design_Active_SOA.gds')
