




import nazca as nd
import Frame_for_tile
def EBL_tile(title):
    with nd.Cell( name = "EBL single tile") as EBL_single_tile:
        nd.add_layer(name="EBL_Tile_AM", layer=1, accuracy=0.001)
        nd.add_layer(name="EBL_Tile_Frame", layer=4, accuracy=0.001)
        nd.add_layer(name="EBL_Tile_Bars", layer=2, accuracy=0.001)
        nd.add_layer(name="EBL_Tile_Name", layer=3, accuracy=0.001)
        horizonatal_lines= False
        square_distance_of_am = 3000
        centerized_alignment_mark = -20/2

        square_box_size = 20
        sbs = square_box_size

        # nw_am = nd.strt(length = sbs, width = sbs, layer = "EBL_Tile_AM").put(centerized_alignment_mark - square_distance_of_am , square_distance_of_am)
        # ne_am = nd.strt(length = sbs, width = sbs, layer = "EBL_Tile_AM").put(centerized_alignment_mark + square_distance_of_am, square_distance_of_am)
        # sw_am = nd.strt(length = sbs, width = sbs, layer = "EBL_Tile_AM").put(centerized_alignment_mark - square_distance_of_am , - square_distance_of_am)
        # se_am = nd.strt(length = sbs, width = sbs, layer = "EBL_Tile_AM").put(centerized_alignment_mark + square_distance_of_am , - square_distance_of_am)


        clearance_am = 120
        frame_length = 2*(square_distance_of_am+clearance_am + sbs/2)
        frame_width = 2*(square_distance_of_am+clearance_am + sbs/2)
        frame_thickness = 50
        centerized_frame =-frame_length/2
        Frame_for_tile.frafrafra(frame_length, frame_width, frame_thickness, "EBL_Tile_Frame").put(centerized_frame, centerized_frame)


        if horizonatal_lines:
            horizontal_top_title_line = nd.strt(length = 260+50, width =50, layer = "EBL_Tile_Bars").put( -frame_width/2 , 2265+580)
            horizontal_top_title_line = nd.strt(length = 260+50, width =50, layer = "EBL_Tile_Bars").put( -frame_width/2 , 2265+580-5690)
            horizontal_top_title_line = nd.strt(length = 260+50, width =50, layer = "EBL_Tile_Bars").put( -frame_width/2 +5950, 2265+580)
            horizontal_top_title_line = nd.strt(length = 260+50, width =50, layer = "EBL_Tile_Bars").put( -frame_width/2 +5950, 2265+580-5690)

            vertical_bar_left1 = nd.strt(length=50, width=240 + 20, layer="EBL_Tile_Bars").put(
                centerized_alignment_mark - square_distance_of_am + square_box_size + clearance_am, -3000)
            vertical_bar_left1 = nd.strt(length=50, width=240 + 20, layer="EBL_Tile_Bars").put(
                centerized_alignment_mark - square_distance_of_am + square_box_size + clearance_am, 3000)
            vertical_bar_right1 = nd.strt(length=50, width=240 + 20, layer="EBL_Tile_Bars").put(
                centerized_alignment_mark + square_distance_of_am - clearance_am - frame_thickness, 3000)
            vertical_bar_right1 = nd.strt(length=50, width=240 + 20, layer="EBL_Tile_Bars").put(
                centerized_alignment_mark + square_distance_of_am - clearance_am - frame_thickness, -3000)

        title = nd.text("{}".format(title), height= 200, layer = "EBL_Tile_Name", align="cc").put(-2001.892-206.036-130+50+70,+2600+360)

    #EBL_single_tile.put(0,0)

    return EBL_single_tile


title = " "
EBL_tile(title)

# nd.strt(length  = 500000 , width = 0.1, layer = 111).put(-100000/2,0)
# nd.strt(width  = 500000 , length = 0.1, layer = 111).put(-0.1/2,0)


nd.export_gds(filename=r'EBL_MapV1_Frame')
# nd.export_gds(filename=r'EBL_Map_Alex')
