
size_of_wafer = 3
diameter_wafer = size_of_wafer * 2.54*10000
radius_wafer = diameter_wafer

xy_tile_direction = 6310 #The initial position of the wafer is in the center of the wafer. The size of the tile in
# x and y directions is 6360 but I removed 50um to overlap the tiles so the cutting lane is 50um.
starting_pos_x = xy_tile_direction/2
starting_pos_y = xy_tile_direction/2
step_for_each_tile = xy_tile_direction
range_in_i = 20
range_in_j = 20
#Q1 =================================================================================
for i in range(range_in_i):
    for j in range(range_in_j):
        if (i*starting_pos_x)**2 + (j*starting_pos_y)**2 < radius_wafer**2:
            print(( i*starting_pos_x)**2 + (j*starting_pos_y)**2, "< \n", radius_wafer**2, "yes")
        else:
            print(( i*starting_pos_x)**2 + (j*starting_pos_y)**2, "< \n", radius_wafer**2, "no")
