import math
import nazca.geometries as geom

from Single_PAM_EBL import PreAM
import nazca as nd
from doted_circle import dotted_circle as dw
from Pattern_Map_EBL_V3 import EBL_PatternMAp_V3
import math

nd.Polygon(layer=36, points=geom.circle(radius=38100,N=1000)).put(10,10)
size_of_wafer = 3
rows_of_devices = 30
cols_of_devices = 30
gap_between_devices = 320
excluded_devices = [(19,13),(19,14),(19,18),(19,19),(18,20),(17,20),(14,20),(13,20),(18,11),(17,11),(14,11),(13,11),(12,13),(12,14),(12,17),(12,19)]

dw(443,size_of_wafer).put(0,0)
List_Of_Coordinates_Pre_AMs = [(-26250,-23250),(-26250,23250),(26250,23250),(26250,-23250)]
with nd.Cell(name = "Pre Alignment Marks 4 Corners") as PAMs:
    for x_y_Coordinates in List_Of_Coordinates_Pre_AMs:
        PreAM(1).put(x_y_Coordinates)
        nd.Pin('{}'.format(x_y_Coordinates)).put(x_y_Coordinates)
        nd.put_stub()
PAMs.put(0,0)
def Centered_AM(layer):
    with nd.Cell(name = "Centered AM") as Centered_AM:
        square_size = 20
        nd.strt(length = square_size, width = square_size, layer = layer).put(-square_size/2,0)
    return Centered_AM
Centered_AM(1).put(0,0)
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
for x_y_coords in List_Coordinates_Coarse_Fine_AMs:
    Centered_AM(1).put(x_y_coords)
    nd.Pin('{}'.format(x_y_coords)).put(x_y_coords)
    nd.put_stub()


def array_devices(num_cols,num_rows, distance_between_devices, excluded_devices, show_pin_centers = True, show_names_matrix = True,size_of_wafer=3):
    number_of_devices_rows = num_rows
    number_of_devices_columns = num_cols
    distance_between_designing_areas = distance_between_devices
    dbda = distance_between_designing_areas
    frame_size = 6000
    # how_many_devices_can_fit_in_three_inches =

    am_layer = 5
    frame_layer = 33
    centering_value_x =  -((num_cols)*frame_size+(num_cols-1)*dbda)/2
    centering_value_y =  -((num_rows)*frame_size+(num_rows-1)*dbda)/2
    additional_exclusion = 5000
    k=1
    posx = frame_size / 2 + centering_value_x
    for i in range(1,number_of_devices_rows+1):
        posy = frame_size/2+centering_value_y
        for j in range(1,number_of_devices_columns+1):
            wafer_radius = (size_of_wafer * 2.54 * 10000)/2
            current_radius = math.sqrt(posx**2+posy**2)
            if current_radius< wafer_radius-additional_exclusion:
                if (j,i) not in excluded_devices:
                    Devices = EBL_PatternMAp_V3(am_layer,frame_layer,frame_size,True, False).put(posx,posy)
                    nd.Pin('{},{}'.format(posx, posy)).put(posx, posy)
                    if show_names_matrix:
                        text_layer = 333
                        text_height = 500
                        nd.text("i,j coords:{},{}\n x,y coords {},{} \n Radius {} ,\n Device num {}".format(j,i,k,posx,posy, k), layer = text_layer, height = text_height/5).put(posx,posy)
                    k=k+1
                    if show_pin_centers:
                        nd.put_stub()
            posy = posy + dbda + frame_size
        posx = posx + dbda + frame_size


array_devices(rows_of_devices,cols_of_devices,gap_between_devices,excluded_devices,False, True,size_of_wafer)





nd.export_gds(filename='Full_Wafer_MAP_EBL_V1.gds', clear = False)
nd.export_svg(path='output', title='3-inch Circle Design with Center Marker')
