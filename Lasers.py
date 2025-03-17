import nazca as nd
import nazca.geometries as geo





nd.add_layer(name = "Designing Area for EBL", layer = 1)
nd.add_layer(name = "Waveguide", layer = 2)
nd.add_layer(name = "SiO Opening", layer = 3)
nd.add_layer(name = "P-Metallization", layer = 4)
nd.add_layer(name = "N-Metallization", layer = 5)
nd.add_layer(name = "Cutting Lanes", layer = 6)
nd.add_layer(name = "EBL AM", layer = 7)
nd.add_layer(name = "VTEC LOGO", layer = 8)
nd.add_layer(name = "Test_Layer", layer = 20)


##########Beggin_Frame
frame_L = 3800
frame_W = 3800
box = geo.frame(100, frame_L, frame_W)
nd.Polygon(box, layer="Designing Area for EBL").put()
###########End_Frame

def Lasers(gap, length, frame_width):
    with nd.Cell(name="Lasers length {}".format(length)) as Lasers_Length:
        frame_width = frame_width
        additional_wvg_cutting_lane = 25
        additional_wvg_cutting_lane_metal = 20
        ground_metal_width = 100
        distance_between_SOAs = gap
        ground_metal_line_width = 70
        ground_metal_line_length = 40
        SOA_metallization_width = 100
        other_side_metallization = 4
        distance_SOAmetal_GROUNDmetal = 25

        gmw = ground_metal_width
        awcl = additional_wvg_cutting_lane
        awclm = additional_wvg_cutting_lane_metal
        gmlw = ground_metal_line_width
        gmll = ground_metal_line_length
        dsg = distance_SOAmetal_GROUNDmetal
        osm = other_side_metallization
        Smw = SOA_metallization_width
        num_of_devices = frame_width // distance_between_SOAs
        SOA_width = []
        k = 0
        for i in range(num_of_devices):
            print(i)
            if 1.5 + k * 0.25 <= 2.5:
                SOA_width.append(1.5 + k * 0.25)
                k = k + 1
            else:
                k = 0
                SOA_width.append(1.5 + k * 0.25)
                k = k + 1
        for i in range(num_of_devices):
            text_linewidth =25
            with nd.Cell(name="Laser") as Laser:
                metallization_len = length
                ground_x_dir = 0
                ground_y_dir = -gmw / 2-SOA_width[i]/2-osm-dsg
                text1_x = +20 #metallization_len/7
                text1_y = Smw+15
                wvg_len = metallization_len+2*awcl
                wvg = nd.strt(length = wvg_len, width = SOA_width[i], layer ="Waveguide").put(metallization_len-wvg_len+awcl,0)
                SiO_Openings = nd.strt(length=metallization_len + 2*awclm, width=SOA_width[i] * 0.75, layer='SiO Opening').put(-awclm,0)
                Metallization = nd.strt(length=metallization_len + 2*awclm, width=Smw, layer='P-Metallization').put(-awclm, +Smw / 2 - SOA_width[i] / 2-osm)
                ground_metal = nd.strt(length=metallization_len, width=gmw, layer=16).put(ground_x_dir, ground_y_dir)
                ground_sio_open = nd.strt(length=metallization_len - 10, width=gmw-10, layer=15).put(+ground_x_dir+5,ground_y_dir)
                ground_sio_bottom_open = nd.strt(length=metallization_len - 10 - 10, width=gmw -20, layer=14).put(ground_x_dir+10,ground_y_dir)
                nd.text("SOA W:{} L:{}".format(SOA_width[i],length, awclm), height =text_linewidth, layer="P-Metallization").put(text1_x,text1_y)
            Laser.put(0, (i + 1) * distance_between_SOAs - 130 - 190 / 2 + 62.75+170/2-(+93-37.25)/2)
            cutting_lane_1 = nd.strt(length=50, width=3700, layer="Cutting Lanes").put(-50, 3700 / 2)
            cutting_lane_1_5 = nd.strt(length=50, width=3700, layer="Cutting Lanes").put(length, 3700 / 2)

        return Lasers_Length
Lasers_length = [250,400, 500,600,750,1000]
cutting_lane_length = 50
x = 0
for laser_len in Lasers_length:
    Lasers(300,laser_len).put(x + Lasers_length.index(laser_len)*cutting_lane_length,0)
    x = x + laser_len
    # Lasers(300,laser_len).put(500+50,0)
    # Lasers(300,laser_len).put(500+750+100,0)
















