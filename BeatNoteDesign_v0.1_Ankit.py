### Beat note Detector Mask Design ###
### Date: 2024-07-25


import nazca as nd
import nazca.geometries as geo
import math
import csv
from math import sin, pi
from collections import defaultdict

nd.add_layer2xsection(xsection='XS1', layer=1, accuracy=0.00001)
nd.logfile()

# create layers:
nd.add_layer(name='lay1', layer=1)
nd.add_layer(name='lay2', layer=2, accuracy=0.01)
nd.add_layer(name='lay222', layer=7, accuracy=0.01)
nd.add_layer(name='lay2222', layer=10, accuracy=0.01)
nd.add_layer(name='lay3', layer=3)
nd.add_layer(name='lay5', layer=5)
nd.add_layer(name='lay6', layer=6)

# create xs + interconnect
nd.add_xsection('xs1')
# nd.add_layer2xsection(xsection='xs1', layer='lay1')
nd.add_layer2xsection(xsection='xs1', layer='lay2', growx=0)

ic = nd.interconnects.Interconnect(xs='xs1', radius=500, width=2.0)

# create inverted xs + interconnect
nd.add_xsection('xs1i')
nd.add_layer2xsection(xsection='xs1i', layer='lay3', leftedge=(0.5, 0), rightedge=(0.5, 5))
nd.add_layer2xsection(xsection='xs1i', layer='lay3', leftedge=(-0.5, 0), rightedge=(-0.5, -5))
ici = nd.interconnects.Interconnect(xs='xs1i', radius=50, width=2.0)
metal=True

def angled_waveguide(angle=7,length=50,width1=2,width2=2,length2=1,text=False,ID='ID'):
    with nd.Cell('Slanted WG') as C:
        inp=ic.strt(length=100,width=3).put(0,0,angle)
        ic.taper(length=length, width1=width1,width2=width2).put()
        angled=ic.bend(angle=angle,width=width2).put()
        out=ic.strt(length=length2,width=width2).put()



        #nd.strt(length= length2-100, width = width, layer = 123).put(angled.pin['b0'])

        nd.Pin(name='a0', width=width1, xs='shallow').put(inp.pin['a0'])
        nd.Pin(name='b0', width=width2, xs='shallow').put(out.pin['b0'])

        if text==True and angle==0:
            nd.text(text=ID, height=10, layer='lay1').put(265-150, -60-30-10, 90, flip = 1)
        elif text==True and angle!=0:
            nd.text(text=ID, height=10, layer='lay1').put(265-100, 20-50-70,2*angle+90,flip=1)

    return C




def vtec_mmi_1x2(mmi_section=90,width_mmi=8, width=2,angle=7,inp_wg=100,out_wg=10,width1=2,text=True,ID='ID'):
    with nd.Cell('mmi_1x2') as mmi_1x2:
        length = mmi_section
        offset = 1.6
        wio = width+.5
        # l = taper_len.ptaper_length(w0=width, w1=wio)
        l = 10

        if angle==0:
            taper_in_1 = ic.taper(width1=width1, width2=width, length=inp_wg).put()

        else: 
            taper_in_1 = angled_waveguide(angle=angle,width1=width1,width2=width,length=inp_wg).put(flop=0,flip=1 , metal = False)
        ic.taper(width1=width, width2=width+.5, length=l).put()
        mm_section = ic.strt(width=width_mmi, length=length).put()
        ic.taper(width1=wio, width2=width, length=l).put(0, -width_mmi/4, 0,mm_section.pin['b0'])
        taper_out_1 = ic.strt(width=width, length=out_wg).put()
        ic.taper(width1=wio, width2=width, length=l).put(0,width_mmi/4, 0,mm_section.pin['b0'])
        taper_out_2 = ic.strt(width=width, length=out_wg).put()


        nd.Pin(name='a0', width=width, xs='shallow').put(taper_in_1.pin['a0'])
        nd.Pin(name='b0', width=width, xs='shallow').put(taper_out_1.pin['b0'])
        nd.Pin(name='b1', width=width, xs='shallow').put(taper_out_2.pin['b0'])
        if text==True and angle==0:
            nd.text(text=ID, height=15, layer='lay1').put(265, 20)
        elif text==True and angle!=0:
            nd.text(text=ID, height=15, layer='lay1').put(265, 20,-angle)

        # nd.put_stub(pinname='b1')
        # nd.put_stub(pinname='b0')
        # nd.put_stub(pinname='a0')


        return mmi_1x2

def omega(length=100,width=2):
    with nd.Cell('Omega') as C:
        bend1=ic.sbend(width=width).put(0,0,0)
        ic.strt(length=length,width=width).put()
        ic.bend(angle=-180,width=width).put()
        ic.strt(length=400+2*length,width=width).put()
        ic.bend(angle=-180,width=width).put()
        ic.strt(length=length,width=width).put()
        bend2=ic.bend(angle=180,width=width).put()
        nd.Pin(name='a0', width=width, xs='shallow').put(bend1.pin['a0'])
        nd.Pin(name='b0', width=width, xs='shallow').put(bend2.pin['b0'])
    return C

def eopm(length=750, width=2, radius=500,text=True,ID='ID'):
    with nd.Cell('EOPM') as eopm:
        inp=ic.taper(length=100,width1=3,width2=3).put(0,0)
        ic.taper(length=50,width1=3,width2=width).put()
        mmi1=vtec_mmi_1x2(angle=0,inp_wg=10,out_wg=0,width=width,width1=width,text=text,ID=ID).put()
        mmi2=vtec_mmi_1x2(angle=0,inp_wg=150,out_wg=0,width=width,width1=width).put(mmi1.pin['a0'].move(-length-250),flip=1)
        ic.strt_p2p(mmi1.pin['b1'],mmi2.pin['b1'],width=width).put()

        nd.strt(length = 620, width = width*0.75, layer = 'lay222').put(mmi1.pin['b1'],flip=1)
        nd.strt(length = 620, width = width, layer = 'lay2222').put(mmi1.pin['b1'],flip=1)

        sbend1=ic.sbend(radius=radius,width=width).put(mmi1.pin['b0'],flip=1)
        sbend2=ic.sbend(radius=radius,width=width).put(mmi2.pin['b0'],flip=0)
        ic.strt_p2p(sbend1.pin['b0'],width=width).put()


        x,y,a = nd.diff(sbend1.pin['b0'],sbend2.pin['b0'])
        angle1 = ((620-x)/(4*radius))
        angle = math.asin(angle1)
        sbend1a=nd.bend(radius=radius,width=width*0.75, layer = 'lay222', angle = angle*180/pi).put(mmi1.pin['b0'],flip=1)
        sbend1b=nd.bend(radius=radius,width=width*0.75, layer = 'lay222', angle = angle*180/pi).put()



        SiO_openings = nd.strt(length = x, width = width*0.75, layer = 'lay222').put(sbend1.pin['b0'])

        sbend1a = nd.bend(radius=radius, width=width*0.75, layer='lay222', angle= angle*180/pi).put()
        sbend1b = nd.bend(radius=radius, width=width*0.75, layer='lay222', angle=angle*180/pi).put(sbend1a.pin['b0'],flip=1)
        #########################################################################
        sbend1a=nd.bend(radius=radius,width=width, layer = 'lay2222', angle = angle*180/pi).put(mmi1.pin['b0'],flip=1)
        sbend1b=nd.bend(radius=radius,width=width, layer = 'lay2222', angle = angle*180/pi).put()

        Metallization = nd.strt(length = x, width = width, layer = 'lay2222').put(sbend1.pin['b0'])

        sbend1a = nd.bend(radius=radius, width=width, layer='lay2222', angle= angle*180/pi).put()
        sbend1b = nd.bend(radius=radius, width=width, layer='lay2222', angle=angle*180/pi).put(sbend1a.pin['b0'],flip=1)



        ######################## GROUNDS
        nd.strt(length = 620, width = 50, layer = 15).put(270,80)
        nd.strt(length = 610, width = 40, layer = 14).put(270+5,80)
        nd.strt(length = 630, width = 60, layer = 16).put(270-5,80)


        # ic.strt_p2p(mmi2.pin['b0']).put()
        # out=ic.strt(length=100,width=width).put(mmi2.pin['b0'])
        nd.Pin(name='a0', width=width, xs='shallow').put(inp.pin['a0'])
        # nd.Pin(name='b0', width=width, xs='shallow').put(out.pin['b0'])
    return eopm



def grating(pitch=1, duty_cycle=.5, radius=30, N=50, angle=30):
    with nd.Cell('Grating') as Grating:
        w = pitch
        pitch = pitch / .7645

        for i in range(N):
            nd.bend(radius=radius + pitch * i * math.sin(math.radians(90 - angle)), angle=angle, width=w * duty_cycle,
                    xs='XS1').put(
                -pitch * 3.14 * i / 32 * 0,
                -i * pitch * math.sin(math.radians(90 - angle)))
        poly = geo.pie(radius=radius + pitch * i * math.sin(math.radians(90 - angle)) + w / 2, angle=angle)
        nd.Polygon(poly, layer='lay1').put(0, radius, -(180 - angle))
        nd.Pin('a0').put(0, radius, 90 + angle / 2)
        nd.put_stub()
        r = radius + pitch * i * .707 + w / 2
        nd.Pin('b0').put(3.14 * r / 8 - 1, -r / 2, 180 + 90 + angle / 2)
        nd.put_stub()
    return Grating
def Metal_corners(layer):
    with nd.Cell(name  = "Metal Corner") as Metal_Corners:
         nd.strt(length = 200, width = 50-25, layer  = layer).put(0,-25/2)
         nd.strt(length = 175, width = 50, layer  = layer).put(0,-25+50)
         nd.strt(length = 125, width = 50, layer  = layer).put(0,-25+50+50)
         nd.strt(length = 75, width = 50, layer  = layer).put(0,-25+50+50+50)
         nd.strt(length=25, width=25, layer=layer).put(0,50+25+50+50-25/2)
    if layer == 'Open Corners':
            nd.strt(length=50, width=250, layer=layer).put(-50, 250/2-50)

    return Metal_Corners

def Metal_corners_hole(layer):

    with nd.Cell(name="Metal Corner Holes") as Metal_Corners_Holes:
        nd.strt(length=200, width=25, layer=layer).put(0,-25/2)
        nd.strt(length=175, width=50, layer=layer).put(25,25)
        nd.strt(length=125, width=50, layer=layer).put(25+50,25+50)
        nd.strt(length=75, width=50, layer=layer).put(25+50+50,25+50+50)
        nd.strt(length=25, width=25, layer=layer).put(25+50+50+50,50+25+50+50-25/2)
    return Metal_Corners_Holes
def Metal_cornersl(layer):
    with nd.Cell(name  = "Metal Corner") as Metal_Corners:
         #nd.strt(length = 200, width = 50-25, layer  = layer).put(0,-25/2)
         ##nd.strt(length = 175, width = 50, layer  = layer).put(0,-25+50)
         #nd.strt(length = 125, width = 50, layer  = layer).put(0,-25+50+50)
         #nd.strt(length = 75, width = 50, layer  = layer).put(0,-25+50+50+50)
        # nd.strt(length=25, width=25, layer=layer).put(0,50+25+50+50-25/2)
         nd.strt(length = 200, width = 50-25, layer  = layer).put(0,50+25+50+50-25/2)
         nd.strt(length = 175, width = 50, layer  = layer).put(0,-25+50+50+50)
         nd.strt(length = 125, width = 50, layer  = layer).put(0,-25+50+50)
         nd.strt(length = 75, width = 50, layer  = layer).put(0,-25+50)
         nd.strt(length=25, width=25, layer=layer).put(0,-25/2)
    if layer == 'Open Corners':
            nd.strt(length=50, width=250, layer=layer).put(-50, 250/2-50)

    return Metal_Corners

def Metal_corners_holel(layer):

    with nd.Cell(name="Metal Corner Holes") as Metal_Corners_Holes:
        #nd.strt(length=200, width=25, layer=layer).put(0,-25/2)
       # nd.strt(length=175, width=50, layer=layer).put(25,25)
       # nd.strt(length=125, width=50, layer=layer).put(25+50,25+50)
      ##  nd.strt(length=75, width=50, layer=layer).put(25+50+50,25+50+50)
        #nd.strt(length=25, width=25, layer=layer).put(25+50+50+50,50+25+50+50-25/2)
        nd.strt(length=200, width=25, layer=layer).put(25+50+50+50,50+25+50+50-25/2)
        nd.strt(length=175, width=50, layer=layer).put(25+50+50+75,25+50+50)
        nd.strt(length=125, width=50, layer=layer).put(25+50+175,25+50)
        nd.strt(length=75, width=50, layer=layer).put(25+275,25)
        nd.strt(length=25, width=25, layer=layer).put(350,-25/2)
    return Metal_Corners_Holes
def Metal_cornersd(layer):
    with nd.Cell(name  = "Metal Corner") as Metal_Corners:
         #nd.strt(length = 200, width = 50-25, layer  = layer).put(0,-25/2)
         ##nd.strt(length = 175, width = 50, layer  = layer).put(0,-25+50)
         #nd.strt(length = 125, width = 50, layer  = layer).put(0,-25+50+50)
         #nd.strt(length = 75, width = 50, layer  = layer).put(0,-25+50+50+50)
        # nd.strt(length=25, width=25, layer=layer).put(0,50+25+50+50-25/2)
         #nd.strt(length = 25, width = 200, layer  = layer).put(0,50+25+50+50-25/2)
        # nd.strt(length =50, width = 175, layer  = layer).put(25,50+50+50)
         #nd.strt(length = 50, width = 125, layer  = layer).put(75,50+50+25)
         nd.strt(length = 50, width = 75, layer  = layer).put(125,100)
         nd.strt(length=25, width=25, layer=layer).put(175,75)
    if layer == 'Open Corners':
            nd.strt(length=50, width=250, layer=layer).put(-50, 250/2-50)

    return Metal_Corners

def Metal_corners_holed(layer):

    with nd.Cell(name="Metal Corner Holes") as Metal_Corners_Holes:
        #nd.strt(length=200, width=25, layer=layer).put(0,-25/2)
       # nd.strt(length=175, width=50, layer=layer).put(25,25)
       # nd.strt(length=125, width=50, layer=layer).put(25+50,25+50)
      ##  nd.strt(length=75, width=50, layer=layer).put(25+50+50,25+50+50)
        #nd.strt(length=25, width=25, layer=layer).put(25+50+50+50,50+25+50+50-25/2)
       # nd.strt(length=25, width=200, layer=layer).put(25+50+50+50,50+25+50+50-25/2)
        #nd.strt(length=50, width=175, layer=layer).put(25+50+50+75,25+50+50+50)
        #nd.strt(length=50, width=125, layer=layer).put(25+50+175,25+175)
        nd.strt(length=50, width=75, layer=layer).put(25+275,25+75+125)
        nd.strt(length=25, width=25, layer=layer).put(350,75+175)
    return Metal_Corners_Holes

def alignemnt_mark(length=200, width=100, inverse=0):
    with nd.Cell('Markers') as C:
        box = geo.box(length=length, width=width)
        box1 = geo.box(length=width, width=length)

        nd.Polygon(box, layer='lay1').put(0)
        nd.Polygon(box1, layer='lay1').put(length / 2 - width / 2)

        if inverse:
            clad = geo.box(length + 50, length + 50)
            nd.Polygon(points=clad, layer='lay2').put(-25)
            pgons = merge_polygons(cell=C, layers=['lay1', 'lay2'])
            remove_polygons(cell=C, layers=['lay1', 'lay2'])  # optional
            pdiff = nd.clipper.diff_polygons(pgons['lay2'], pgons['lay1'])
            for pol in pdiff:
                nd.Polygon(points=pol, layer=7).put(0)
    return C

with nd.Cell('VTEC Logo') as vtec_logo:
            [nd.text('V  T  E  C', height=100, align='rb', layer=1).put(95, 0)
             for layer in [1]]
            [nd.text('LASERS & SENSORS', height=50, align='rb', layer=1).put(120, -50)
             for layer in [1]]
            outline = [(0, 0), (0, 10), (8.7, 15), (8.7, 25), (17.4, 30), (0, 40), (-17.4, 30), (-17.4, 10), (0, 0),
                       (0, 10),
                       (-8.7, 15), (-8.7, 25), (0, 30), (8.7, 25), (8.7, 15), (0, 10), (-8.7, 15), (0, 20), (0, 30),
                       (8.7, 25),
                       (8.7, 15), (0, 10)]
            nd.Polygon(layer=1, points=outline).put(-450, -50, scale=4)
        

#alignemnt_mark().put()
frame_L = 3800
frame_W = 3800
gap = 500
box = geo.frame(100, frame_L, frame_W)
nd.Polygon(box, layer=6).put()

alignemnt_mark(length=100, width=10).put(frame_L / 2 - 150, frame_W  - 200)
alignemnt_mark(length=100, width=10).put(frame_L / 2 - 150, 150)
alignemnt_mark(length=100, width=10).put(frame_L - 150 - 150, frame_W - 200)
alignemnt_mark(length=100, width=10).put(frame_L - 150 - 150,  150)
#nd.image(r'C:/Users/Vtec/Desktop\spectriK_logo.png',threshold=0.3, layer=1,size=500, pixelsize=2.3).put(frame_L - 75 - 205, 2400, 270)

Metal_corners(2).put(frame_L / 2-200+1625 , frame_W-3975 )
Metal_corners(2).put(frame_L / 2-225 , frame_W-3975 )
Metal_corners(2).put(frame_L / 2-825, frame_W-3975 )
Metal_corners(2).put(frame_L / 2-1425, frame_W-3975 )
Metal_corners(2).put(frame_L / 2-1925 , frame_W-3975 )
Metal_corners(2).put(frame_L / 2-200+1025 , frame_W-3975 )
Metal_corners(2).put(frame_L / 2-200+3025-950 , frame_W-3975 )
Metal_corners_hole(22).put(frame_L / 2 + 800+350+25, frame_W -3975)
Metal_corners_hole(22).put(frame_L / 2 -100+675, frame_W -3975)
Metal_corners_hole(22).put(frame_L / 2 + 1725-125+25, frame_W-3975)
Metal_corners_hole(22).put(frame_L / 2 -700+225, frame_W -3975)
Metal_corners_hole(22).put(frame_L / 2 -1200+125, frame_W -3975)
Metal_corners_hole(22).put(frame_L / 2-1700+25 , frame_W-3975 )
Metal_corners_hole(22).put(frame_L / 2-1700-500+25 , frame_W-3975 )
#upper metal corners 
Metal_cornersl(2).put(frame_L / 2-200+1625 , frame_W-200+125  )
Metal_cornersl(2).put(frame_L / 2-225 , frame_W-200+125  )
Metal_cornersl(2).put(frame_L / 2-825, frame_W-200+125  )
Metal_cornersl(2).put(frame_L / 2-1425, frame_W-200+125  )
Metal_cornersl(2).put(frame_L / 2-1925 , frame_W-200+125  )
Metal_cornersl(2).put(frame_L / 2-200+1025 , frame_W-200+125)
Metal_corners_holel(22).put(frame_L / 2 + 800+350-175+25, frame_W-200+125)
Metal_corners_holel(22).put(frame_L / 2 -100+650-175+25, frame_W-200+125)
Metal_corners_holel(22).put(frame_L / 2 + 1700-175-125+50, frame_W-200+125)
Metal_corners_holel(22).put(frame_L / 2 -700+200-175+25, frame_W-200+125)
Metal_corners_holel(22).put(frame_L / 2 -1200+100-175+25, frame_W-200+125)
Metal_corners_holel(22).put(frame_L / 2-1700-175+25 , frame_W-200+125)
Metal_corners_holel(22).put(frame_L / 2-1700-500+25-175 , frame_W-200+125 )
#d metal corners 
for i in range(24):
    Metal_corners_holed(22).put(frame_L / 2-2375 , frame_W-200+125-600-i*150)
    #Metal_corners_holed(22).put(frame_L / 2-2375 , frame_W-200+125-900-i*300)
    Metal_cornersd(2).put(frame_L / 2-2200 , frame_W-400-i*150)
    #Metal_cornersd(2).put(frame_L / 2-2200 , frame_W-400-i*300)
for i in range(24):
    Metal_corners_holed(22).put(frame_L / 2+1150+450, frame_W-200+125-600-i*150)
    #Metal_corners_holed(22).put(frame_L / 2-2375 , frame_W-200+125-900-i*300)
    Metal_cornersd(2).put(frame_L / 2+1325+450 , frame_W-400-i*150)
    #Metal_cornersd(2).put(frame_L / 2-2200 , frame_W-400-i*300)
frame_L = 3800
frame_W = 3800
vtec_logo.put(frame_L - 75 - 250, 1300, 270)
box = geo.box(length=100, width=frame_W-100)
box1 = geo.box(length=400, width=100)
#
#
n_cols = int(1 * frame_L / gap)
print('No of Columns', n_cols)
n_rows = int(frame_W / 150)
offset = 0
chip_ID = 0
angle=7

with open(r'C:\Users\alexa\OneDrive\Desktop\Mask Design Main\PIC_chipsIDs (2).csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(
        ['ChipID','Type', "Length(um)", "Waveguide Width(um)", "MMI Width", "MMI Length", "Radius(um)"])
    for columns in range(n_cols):
        if gap * columns < frame_L:
            # if columns == n_cols / 2 - 1:
            #     offset = 750
            #     nd.Polygon(box, layer=6).put(-50 + 100 + gap * (1 + columns), frame_W / 2)

            # nd.Polygon(box, layer=6).put(-100 + offset + gap * (1 + columns), frame_W / 2)
            W_wgs=[1.75,2,2.25,2.5,3]

            if columns == 0:
                L_mmis=range(85,90,1)
                W_mmis=[7.8,7.9,8,8.1,8.2]  # um
                nd.Polygon(box, layer=6).put(400, frame_W / 2-50)
                for row in range(n_rows - 1):
                    width=W_wgs[row%len(W_wgs)]
                    mmi=vtec_mmi_1x2(out_wg=56.8-25,inp_wg=102-75,width1=3,width=width,mmi_section=L_mmis[row%len(L_mmis)],width_mmi=W_mmis[row%len(W_mmis)],
                                    ID=f"ID:{str(chip_ID)}_W{width}_L{L_mmis[row%len(L_mmis)]}_W{W_mmis[row%len(W_mmis)]}").put(-100 + offset + gap * columns, 50 + 150 * row,angle)
                    ic.sbend(width=width).put(mmi.pin['b0'],flip=1)
                    ic.strt(length=75,width=width).put()
                    ic.sbend(width=width).put(mmi.pin['b1'])
                    ic.strt(length=75,width=width).put()

                    writer.writerow([chip_ID,'MMI','NA',width, W_mmis[row%len(W_mmis)],L_mmis[row%len(L_mmis)],'NA'])
                    # writer.writerow([chip_ID, pitches[row % len(pitches)], 0.5, widths[row % len(widths)], Ns[1], Rs[1]])
                    # Columns with varying width and pitch
                    chip_ID += 1
            if columns == 1:
                nd.Polygon(box, layer=6).put(400, frame_W / 2-50)
                for row in range(n_rows - 1):
                    width=W_wgs[row%len(W_wgs)]
                    length=490
                    ID=f"ID:{str(chip_ID)}_W{width}_L{length}"
                    angled_waveguide(length2=length,width1=3,width2=width,text=True,ID=ID).put( -100+offset + gap * columns, 65 + 150 * row,angle,flip=1)

                    if row != 0:
                        ground_sio_open = nd.strt(length=length - 10-89.816-50-5-5, width=50, layer=15).put(450+150+5+4.83+5, 40 + 150 * row-40+40-5)
                        ground_sio_bottom_open = nd.strt(length=length - 10-89.816-50-5-5-10, width=40, layer=14).put(450+150+5+4.83+5+5, 40 + 150 * row-40+40-5)
                        ground_metal = nd.strt(length=length - 10-89.816-50, width=60, layer=16).put(450+150+4.83+5, 40 + 150 * row-40+40-5)

                    SiO_Openings = nd.strt(length=length - 10-89.816-50, width=width*0.75, layer='lay222').put(-100+offset + gap * columns+209.81637, 65 + 150 * row+22.00745)
                    Metallization = nd.strt(length=length - 10-89.816-50, width=54, layer='lay2222').put(-100+offset + gap * columns+209.81637, 65 + 150 * row+22.00745+(25-width/2)-2)

                    writer.writerow([chip_ID,'Bent Waveguide',length,width, "NA",'NA',"NA"])
                    chip_ID += 1
            if columns == 2:
                nd.Polygon(box, layer=6).put(1000, frame_W / 2-50)
                length=560
                for row in range(n_rows - 1):
                    width=W_wgs[row%len(W_wgs)]
                    ID=f"ID:{str(chip_ID)}_W{width}_L{length}"
                    writer.writerow([chip_ID,'Straight',length,width,'NA', "NA","NA"])
                    angled_waveguide(angle=0,length2=length-10,width1=3,text=True,width2=width,ID=ID).put(1000, 40 + 150 * row,0,flip=1)
                    if row != 0:
                        ground_sio_open = nd.strt(length=length-10-150-10, width=50, layer=15).put(1000+150+5, 40 + 150 * row-40-31/2,0)
                        ground_sio_bottom_open = nd.strt(length=length-10-150-10-10, width=40, layer=14).put(1000+150+5+5, 40 + 150 * row-40-31/2,0)
                        ground_metal = nd.strt(length=length-10-100-50, width=60, layer=16).put(1000+150, 40 + 150 * row-40-31/2,0)

                    SiO_Openings = nd.strt(length = length-10-100-50, width = width*0.75, layer = 'lay222').put(1000+150, 40 + 150 * row,0,flip=1)
                    Metallization = nd.strt(length = length-10-100-50, width = 54, layer = 'lay2222').put(1000+150, 40 + 150 * row +25-width/2-2,0,flip=1)
                    chip_ID += 1
                    
            if columns==3:
                nd.Polygon(box, layer=6).put(1600, frame_W / 2-50)
                radius=[500,550,600,700,800]
                for row in range(int(frame_W/150-1)):
                    width=W_wgs[row%len(W_wgs)]
                    ID=f"ID:{str(chip_ID)}_W{width}_L{L_mmis[row%len(L_mmis)]}_W{W_mmis[row%len(W_mmis)]}_R{radius[row%len(radius)]}"
                    eopm(width=width,radius=radius[row%len(radius)],text=True,ID=ID).put(1600, 65 + 150 * row)
                    writer.writerow([chip_ID,'Phase Modulator','NA',width, W_mmis[row%len(W_mmis)],L_mmis[row%len(L_mmis)],radius[row%len(radius)]])
                    chip_ID += 1
            if columns == 5:
                L_mmis=range(90,95,1)
                nd.Polygon(box, layer=6).put(2650, frame_W / 2-50)

                for row in range(frame_W//150-1):


                    width=W_wgs[row%len(W_wgs)]
                    mmi=vtec_mmi_1x2(out_wg=75,inp_wg=155-75,width1=3,width=width,mmi_section=L_mmis[row%len(L_mmis)],width_mmi=W_mmis[row%len(W_mmis)],
                                    ID=f"ID:{str(chip_ID)}_W{width}_L{L_mmis[row%len(L_mmis)]}_W{W_mmis[row%len(W_mmis)]}").put(2650,  25+150 * row,angle)
                    ic.sbend(width=width).put(mmi.pin['b0'],flip=1)
                    ic.strt(length=75,width=width).put()
                    ic.sbend(width=width).put(mmi.pin['b1'])
                    ic.strt(length=75,width=width).put()
                    writer.writerow([chip_ID,'MMI','NA',width, W_mmis[row%len(W_mmis)],L_mmis[row%len(L_mmis)],'NA'])
                    chip_ID += 1
                nd.Polygon(box, layer=6).put(3250, frame_W / 2-50)

# writer.close()
nd.export_gds(filename='Grating_Design.gds')
