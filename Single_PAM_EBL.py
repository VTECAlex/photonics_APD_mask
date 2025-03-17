import nazca as nd

def PreAM(layer,x_y_Coordinates):
    with nd.Cell("Pre Alignment Mark{}".format(x_y_Coordinates)) as PAM:
        square_length = 20
        square_width = 20
        array_size = 21
        pitch = 75
        zz=0
        additional_per_step = 2

        posy = 0
        for z in range(1, array_size//2+2):
            ii = 0
            posx = 0
            for i in range(1, array_size//2+2):
                Q1 = nd.strt(length = square_length, width=square_width, layer = layer).put(posx- square_length/2, posy)#z*(pitch+square_length)+zz*2)
                #nd.text("{}".format(i), layer =2, height=10).put(posx, posy)
                Q2 = nd.strt(length = square_length, width=square_width, layer = layer).put(-posx- square_length/2, posy)
                Q3 = nd.strt(length = square_length, width=square_width, layer = layer).put(-posx- square_length/2, -posy)
                Q4 = nd.strt(length = square_length, width=square_width, layer = layer).put(posx- square_length/2, -posy)

                posx = posx + pitch + (i-1)*additional_per_step
                if i > 0:
                    ii = ii+1
                # print(i, ii, ii*2)
            posy = posy + pitch+ (z-1)*additional_per_step
            if z>0:
                zz = zz + 1
    return PAM

#PreAM(3).put(0,0)
# PAM.put(0,0)
#nd.export_gds(filename='PAM.gds')
