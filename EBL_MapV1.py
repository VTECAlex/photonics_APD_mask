





import nazca as nd
from EBL_MapV1_Tile import EBL_tile
import EBL_dotted_wafer

size_of_wafer = 3
diameter_of_wafer= size_of_wafer * 2.54 * 10000
radius_of_wafer  = diameter_of_wafer/2
EBL_dotted_wafer.dotted_circle(2,size_of_wafer).put(0,0)


# EBL_tile("title")
xy_tile_direction = 6310 #The initial position of the wafer is in the center of the wafer. The size of the tile in
# x and y directions is 6360 but I removed 50um to overlap the tiles so the cutting lane is 50um.
starting_pos_x = xy_tile_direction/2
starting_pos_y = xy_tile_direction/2
step_for_each_tile = xy_tile_direction
range_in_i =20
range_in_j =20
#Q1 =================================================================================
for i in range(range_in_i):
    for j in range(range_in_j):
        if (i*starting_pos_x)**2+(j*starting_pos_y)**2 < (30000/2)**2:
            #Q1
            EBL_tile("Q1 Tile {},{}".format(i + 1, j + 1)).put(starting_pos_x + i * step_for_each_tile,
                                                               starting_pos_y + j * step_for_each_tile)
            #Q2
            EBL_tile("Q2 Tile {},{}".format(i + 1, j + 1)).put(-starting_pos_x - i * step_for_each_tile,
                                                               starting_pos_y + j * step_for_each_tile)
            #Q3
            EBL_tile("Q3 Tile {},{}".format(i + 1, j + 1)).put(-starting_pos_x - i * step_for_each_tile,
                                                               -starting_pos_y - j * step_for_each_tile)
            #Q4
            EBL_tile("Q4 Tile {},{}".format(i + 1, j + 1)).put(starting_pos_x + i * step_for_each_tile,
                                                               -starting_pos_y - j * step_for_each_tile)

# #Q2 =================================================================================
# for i in range(range_in_i):
#     for j in range(range_in_j):
#
#
# #Q3 =================================================================================
# for i in range(range_in_i):
#     for j in range(range_in_j):
#
#
# #Q4 =================================================================================
# for i in range(range_in_i):
#     for j in range(range_in_j):


nd.export_gds(filename=r'EBL_MapV1')
