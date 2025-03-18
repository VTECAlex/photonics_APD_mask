

import pandas as pd
import os



def coordinates_system(where_to_put):
    size_of_wafer = 3
    size_of_reticle = 6

    # circle_reticle_layer = 65
    # logo_text_height = 3000
    # correction_placement = +300 #Correction on when the Logo is placed
    sow = size_of_wafer
    sor = size_of_reticle
    # outer_length = sor * 2.54 * 10000
    # outer_width = sor * 2.54 * 10000
    # inner_length = sow * 2.54 * 10000
    # inner_width = sow * 2.54 * 10000
    diameter_of_wafer= sow * 2.54 * 10000
    radius_of_wafer  = diameter_of_wafer/2
    # ring_width = 21000


    tile_full_length_x_dir = 2100+(2756.294-2100)
    tile_full_length_y_dir = 4900
    pos1x_Q1 = tile_full_length_x_dir/2+1250+30
    pos1y_Q1 = tile_full_length_y_dir/2+50+1250+30+50
    # step_x = tile_full_length_x_dir
    step_y = tile_full_length_y_dir
            
    # emtpy_list = []

    Total_per_Quadrant = 0

    # length_variation = [0,200,500,800,1000,0,200,500,800,1000,0,200,500,800,1000,0,200]



    ########For the PCM tile
    tile_full_length_x_dir_PCM = 6900+380
    tile_full_length_y_dir_PCM = 4800
    pos1x_Q1_PCM = tile_full_length_x_dir_PCM/2+50+1250+30-2580/2-500
    pos1y_Q1_PCM = tile_full_length_y_dir_PCM/2+1250+30
    step_x = tile_full_length_x_dir_PCM
    step_y = tile_full_length_y_dir_PCM+200
            
    ###########################################################
    names_and_coordinates_list = []

    for j in range(10):
        previous_position_for_Q_1_4 = pos1x_Q1 # previous positions for 1 and 4 quadrants Tile
        previous_position_for_Q_2_3 = pos1x_Q1 # previous positions for 2 and 3 quadrants Tile
        x_directio_length_of_all_tiles = 3350 # This is the starting position of the bottom right corner of the center of the tile
        previous_position_for_Q_1_4_PCM = pos1x_Q1_PCM # previous positions for 1 and 4 quadrants PCM
        previous_position_for_Q_2_3_PCM = pos1x_Q1_PCM # previous positions for 2 and 3 quadrants PCM
        x_directio_length_of_all_tiles_PCM = 0
        for i in range(17):
            extra_length =0
            x_directio_length_of_all_tiles  = x_directio_length_of_all_tiles + (tile_full_length_x_dir + extra_length ) 
            y_directio_length_of_all_tiles  = (j+1)*(tile_full_length_y_dir)
            x_directio_length_of_all_tiles_PCM  = x_directio_length_of_all_tiles_PCM + (tile_full_length_x_dir_PCM + extra_length )
            if (x_directio_length_of_all_tiles)**2+(y_directio_length_of_all_tiles)**2< (radius_of_wafer)**2: #This is x^2+y^2<r^2 so we have devices insied the r=4''/2
                Q1 = 1
                Q2 = 2
                Q3 = 3
                Q4 = 4
                if j!=3:
                    #Device_Tile_V3_N_Sub.APD_Tile_V2(extra_length, Q1, i, j, True, True).put(previous_position_for_Q_1_4 + extra_length/2 -15-328.147, pos1y_Q1 + j*step_y -1830 )
                    names_and_coordinates_list.append(["R{}C{}Q{}".format(Q1, i, j),
                                                    previous_position_for_Q_1_4 + extra_length / 2 - 15 - 328.147 + 242.3 + 50,
                                                    pos1y_Q1 + j * step_y - 1830 + 1780 + 50,
                                                    j+1,i+1, Q1])
                    #Device_Tile_V3_N_Sub.APD_Tile_V2(extra_length, Q2, i, j, True, True).put(-previous_position_for_Q_2_3 - extra_length / 2 - 100 - 15 - 328.147, pos1y_Q1 + j * step_y - 1830)
                    names_and_coordinates_list.append(["R{}C{}Q{}".format(Q2, i, j),
                                                    -previous_position_for_Q_2_3 - extra_length / 2 - 100 - 15 - 328.147 + 242.3 + 50,
                                                    pos1y_Q1 + j * step_y - 1830 + 1780 + 50,
                                                    (j+1),-(i+1), Q2])
                    if j<9:
                        #Device_Tile_V3_N_Sub.APD_Tile_V2(extra_length, Q4, i, j, True, True).put(previous_position_for_Q_1_4 + extra_length/2 -15-328.147, -pos1y_Q1 - j*step_y - 1830)
                        # names_and_coordinates_list.append(["R{}C{}Q{}".format(Q4, i, j),
                        #                                 previous_position_for_Q_1_4 + extra_length / 2 - 15 - 328.147 + 242.3 + 50,
                        #                                 pos1y_Q1 + j * step_y - 1830 + 1780 + 50,j+1,i+1, Q4])
                        names_and_coordinates_list.append(["R{}C{}Q{}".format(Q4, i, j),
                                                        previous_position_for_Q_1_4 + extra_length / 2 - 15 - 328.147 + 242.3 + 50,
                                                        -pos1y_Q1 - j * step_y - 1830 + 1780 + 50,
                                                        -(j+1),i+1, Q4])
                        #Device_Tile_V3_N_Sub.APD_Tile_V2(extra_length, Q3, i, j, True, True).put(-previous_position_for_Q_2_3  - extra_length/2 -100 -15-328.147, -pos1y_Q1 - j*step_y - 1830)
                        names_and_coordinates_list.append(["R{}C{}Q{}".format(Q3, i, j),
                                                        -previous_position_for_Q_2_3 - extra_length / 2 - 100 - 15 - 328.147 + 242.3 + 50,
                                                        -pos1y_Q1 - j * step_y - 1830 + 1780 + 50,
                                                        -(j+1),-(i+1), Q3])
                    previous_position_for_Q_1_4 = previous_position_for_Q_1_4 + tile_full_length_x_dir
                    previous_position_for_Q_2_3 = previous_position_for_Q_2_3 + tile_full_length_x_dir
            if (x_directio_length_of_all_tiles_PCM)**2+(y_directio_length_of_all_tiles)**2< (radius_of_wafer)**2:
                Q1 = 1
                Q2 = 4
                Q3 = 2
                Q4 = 3
                if j==3:
                    previous_position_for_Q_1_4_PCM = previous_position_for_Q_1_4_PCM + tile_full_length_x_dir_PCM - 480
                    previous_position_for_Q_2_3_PCM = previous_position_for_Q_2_3_PCM + tile_full_length_x_dir_PCM+100


            Total_per_Quadrant  = Total_per_Quadrant +1
    df = pd.DataFrame(names_and_coordinates_list, columns=["Names","X Coordinate", "Y Coordinate", "Row","Column","Quadrant"])

    return df.to_csv(where_to_put, index=False)







if __name__ == "__main__":
    name_of_the_file = "Coordinates.csv"
    current_directory  = os.getcwd()        
    coordinates_output_file =os.path.join(current_directory,name_of_the_file)
    # name_coordinates = "Coordinates.xlsx"
    coordinates_system(coordinates_output_file)





