from Single_PAM_EBL import PreAM
import nazca as nd
import nazca.geometries as geom
from doted_circle import dotted_circle as dw
from SVG_Pattern_Map_EBL_V3_Active_SOAs import SVG_EBL_PatternMAp_V3_Active_SOAs
import math

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


size_of_wafer = 3
rows_of_devices = 10
cols_of_devices = 10
gap_between_devices_x = 3900 
gap_between_devices_y = 2000
# excluded_devices = [(19,13),
#                     (19,14),
#                     (19,18),
#                     (19,19),
#                     (18,20),
#                     (17,20),
#                     (14,20),
#                     (13,20),
#                     (18,11),
#                     (17,11),
#                     (14,11),
#                     (13,11),
#                     (12,13),
#                     (12,14),
#                     (12,17),
#                     (12,19)]

excluded_devices = [(5,1),
                    (6,1),
                    (9,5),
                    (9,6),
                    (5,10),
                    (6,10)]

dw("Three Inch Wafer",size_of_wafer).put(0,0)
nd.Polygon(layer=36, points=geom.circle(N=300,radius=38100)).put(0,0)
List_Of_Coordinates_Pre_AMs = [(-26250,-23250),
                               (-26250,23250)
                               ,(26250,23250),
                               (26250,-23250)]
with nd.Cell(name = "Pre Alignment Marks 4 Corners") as PAMs:
    for x_y_Coordinates in List_Of_Coordinates_Pre_AMs:
        PreAM("Pre Alignment Mark",x_y_Coordinates).put(x_y_Coordinates)
        nd.Pin('{}'.format(x_y_Coordinates)).put(x_y_Coordinates)
        #nd.put_stub(pinlayer="pinlayer")
PAMs.put(0,0)
def Centered_AM(layer,coords):
    simple_counter = 0
    with nd.Cell(name = "Centered AM{},{}".format(simple_counter,coords)) as Centered_AM:
        square_size = 20
        simple_counter +=1
        nd.strt(length = square_size, width = square_size, layer = layer).put(-square_size/2,0)
    return Centered_AM
#Centered_AM("Centered AM",(0,0)).put(0,0)
List_Coordinates_Coarse_Fine_AMs = [(-25640,-20640),
(-25640,-21490),
(-12360,-20640),
(-25640,-11360),
(-25640,-12210),
(-25640,17400),
(-25640,18250),
(20640,-20640),
(20640,-21490),
(-12360,-21490),
(-12360,20640),
(-12360,21490),
(15360,20640),
(25640,11360),
(25640,12210),
(25640,21250),
(25640,20400),
(25640,-14640),
(25640,-15490),
(15360,21490),
(-15360, 20640),
(-15360, 21490),
(20360, 20640),
(-25640, 11360),
(-25640, 12210),
(-25640, 21250),
(-25640, 20400),
(-25640, -14640),
(-25640, -15490),
(20360, 21490),
(-15640, -20640),
(-15640, -21490),
(12360, -20640),
(25640, -11360),
(25640, -12210),
(25640, 18250),
(25640, 17400),
(25640, -20640),
(25640, -21490),
(12360, -21490),
]
# for x_y_coords in List_Coordinates_Coarse_Fine_AMs:
#     Centered_AM("Coarse and Fine",x_y_coords).put(x_y_coords)
#     nd.Pin('{}'.format(x_y_coords)).put(x_y_coords)
#     nd.put_stub()


def svg_array_devices(num_cols,num_rows,
                  distance_between_devices_x,
                  distance_between_devices_y,
                  excluded_devices,
                  show_pin_centers = True,
                  show_names_matrix = True,
                  size_of_wafer=3,
                  coarse_fine_layer=1,
                  frame_layer=1,
                  text_layer=1,
                  Layer_Pins=1,
                  Layer_SOA_MESA=1,
                  Layer_SOA_SIO_Openings=1,
                  Layer_p_Metallization=1,
                  Layer_n_Metallization=1,
                  Layer_Grounds_SiO_Opening=1,
                  Layer_Grounds_Bottom_SiO_Opening=1,
                  Layer_Cutting_Lanes=1,
                  Layer_Metal_Corners=1,):
    number_of_devices_rows = num_rows
    number_of_devices_columns = num_cols
    distance_between_designing_areas_x = distance_between_devices_x
    dbda_x = distance_between_designing_areas_x
    #dbda_x = 6000
    distance_between_designing_areas_y = distance_between_devices_y
    dbda_y = distance_between_designing_areas_y
    #dbda_y = 9000
    frame_size = 5000
    # how_many_devices_can_fit_in_three_inches =
    centering_value_x =  -((num_cols)*frame_size+(num_cols-1)*dbda_x)/2
    centering_value_y =  -((num_rows)*frame_size+(num_rows-1)*dbda_y)/2
    additional_exclusion = 6000
    k=1
    posx = frame_size / 2 + centering_value_x
    for i in range(1,number_of_devices_rows+1):
        posy = frame_size/2+centering_value_y
        for j in range(1,number_of_devices_columns+1):
            wafer_radius = (size_of_wafer * 2.54 * 10000)/2
            current_radius = math.sqrt(posx**2+posy**2)
            if current_radius< wafer_radius-additional_exclusion:
                switched_coordinates = [(y, x) for x, y in excluded_devices]
                if (j,i) not in switched_coordinates:
                    
                    Devices_Pattern_AMs = SVG_EBL_PatternMAp_V3_Active_SOAs(coarse_fine_layer,
                                                                        frame_layer,
                                                                        frame_size,
                                                                        False,
                                                                        False,
                                                                        posx,
                                                                        posy,
                                                                        Layer_SOA_MESA,
                                                                        Layer_SOA_SIO_Openings,
                                                                        Layer_p_Metallization,
                                                                        Layer_n_Metallization,
                                                                        Layer_Grounds_SiO_Opening,
                                                                        Layer_Grounds_Bottom_SiO_Opening,
                                                                        Layer_Cutting_Lanes,
                                                                        Layer_Metal_Corners,
                                                                        Layer_Pins).put(posx,posy)
                    nd.Pin('{},{}'.format(posx, posy)).put(posx, posy)
                    if show_names_matrix:
                        text_height = 500
                        #nd.text("i,j coords:{},{}\n x,y coords {},{} \n Radius {} ,\n Device num {}".format(j,i,k,posx,posy, k), layer = text_layer, height = text_height/5).put(posx,posy)
                    k=k+1
                    #nd.put_stub(pinshow=show_pin_centers)

            posy = posy + dbda_y + frame_size
        posx = posx + dbda_x + frame_size


svg_array_devices(rows_of_devices,
              cols_of_devices,
              gap_between_devices_x,
              gap_between_devices_y,
              excluded_devices,
              False,
              True,
              size_of_wafer,
              "Pattern",
              "Frame Designing Area",
              "Text Layer",
              "Pin Layer",
              "SOA MESA",
              "SOA SiO Openings",
              "p-Metallization",
              "n-Metallization",
              "Ground SiO Opening",
              "Ground Bottom SiO Opening",
              "Cutting Lanes",
              "Metal Corners")




# print("complete")
# nd.export_gds(filename='Full_Wafer_MAP_EBL_V1_Active_SOAs.gds')
nd.export_gds(filename = "SVG_Full_Wafer_MAP_EBL_V1_Active_SOAs_SELMA.gds")
# nd.export_svg(filename = "SVG_Full_Wafer_MAP_EBL_V1_Active_SOAs_SELMA.svg")

print("Main wafer full map completed")