
import nazca as nd




from ModulationArea import Modulation
from external_connections import ext_con
from MZmodulator import TiPtAuelectrodes
from math import *
from nazca.interconnects import Interconnect

def The_Modulator(length):
    with nd.Cell(name = "Main structure") as Main_Structure:
        extra_line_length = 200
        ell = extra_line_length
    
        length = length
        number = 8
    # =============================================================================
    #     for i in range(length/(number/2)):
    #         length = 
    # =============================================================================
        dist_mmi_wg = 40
        width = 1.5
        distance = 10
        layer = 2
        
        ############### Dimensions for the MMI
        BodyLength = 42.4
        BodyWidth = 6
        LegLength = 10
        LegWidth = width
        DistEdge = 0.75
        
        ########
        electrode_width = 15
        
        ####Dimensions of the modulation area
        distance_waveguides = 50 #distance of the lines
        dw = distance_waveguides #same as above DON'T touchy touchy 
        offset = distance/2 #+width/2 - BodyWidth/2+DistEdge
        esa = +438.5 -8*dw +1.5 # -2* dw  #this term moves the bottom group of lines up and down
        distance_of_the_centers_of_modulators_here = 600
        distance_of_the_centers_of_modulators = distance_of_the_centers_of_modulators_here/distance # DON'T TOUCH
        dcm = distance_of_the_centers_of_modulators
        ic = Interconnect(width = width, radius = 30)
        
        ######## Bent Radius
        Bend_radius = 100
        
        ################# Distance between the legs and the bend in the MMI. It is used to add an extra length on the bend so the Bend and the S-Bend on the modulator to be at the same height
        DIST_BEND_OFFSET = (BodyWidth/2-DistEdge - LegWidth/2)
        
        ############ There is a small missalignement on the output of the middle alignement loop
        small_corecction = 10.906
        ########## Left side
        
        dist_elec_pads = 74.695
        pad_length = 80
        where_move = -13.556
        
        
        
        
        
        Modulation1 = Modulation(number, length, width, distance, layer, BodyLength, BodyWidth, LegLength, LegWidth, DistEdge,dcm,dist_mmi_wg,ell, dist_elec_pads, pad_length, where_move).put()
        #nd.put_stub()
    
        #TiPtAuelectrodes(number, length, width, distance, layer, offset, dcm).put(0, electrode_width/2)
        
        extension_after_mmi = {}
        Bend_after_extenL = {}
        
        
        
        bb = 1000-175+1.5# length_to_find_the_middle/4
        aa= 0
        theta_angle_of_bendR1 = 0
        mass_turn = 250 #How high or low the turn should be
        right_side_regulation_before_turn = -250
        
        
        correction_input_output_aligment =  -60.906000000000006
        last_extension = 592.622-160.906
        
        for i in range(0,number//2):
            #Left side
            extension_after_mmi['extension_L{}'.format(i)] = nd.strt(length = (i)*dw, width = width).put('a0',Modulation1.pin[('mmi0R{}').format(i)])
            #nd.Pin('ext_L{}'.format(i), pin=cc['extension_L{}'.format(i)].pin['b0']).put()
            nd.put_stub()
            #Right side
            extension_after_mmi['extension_R{}'.format(i)] = nd.strt(length = (number//2-i-1)*dw, width = width).put('a0',Modulation1.pin[('mmi0L{}').format(i)])
            #nd.Pin('ext_R{}'.format(i), pin=cc['extension_R{}'.format(i)].pin['b0']).put()
            nd.put_stub()   
        ext_after_bend = {}
        Bend_after_mmi = {}
        for i in range(0,number//2):
            
            if Bend_radius + DIST_BEND_OFFSET <= offset :
                
                extra_addition_after_bend = mass_turn+ DIST_BEND_OFFSET + (offset-Bend_radius)
            else:
                extra_addition_after_bend = mass_turn
            
        
            Bend_after_mmi['Bend_after_mmiL{}'.format(i)] = nd.bend(radius=Bend_radius, angle = -90, width = width).put(extension_after_mmi['extension_L{}'.format(i)].pin['b0'])
            ext_after_bend['ext_after_bend_L{}'.format(i)] = nd.strt(length  = extra_addition_after_bend +i*(distance*dcm), width = width).put(Bend_after_mmi['Bend_after_mmiL{}'.format(i)].pin['b0'])
            Bend_after_mmi['Bend_after_mmiR{}'.format(i)] = nd.bend(radius=Bend_radius, angle = -90, width = width).put(extension_after_mmi['extension_R{}'.format(i)].pin['b0'])
            ext_after_bend['ext_after_bend_R{}'.format(i)] = nd.strt(length  =extra_addition_after_bend +distance*dcm*((number//2)-1-i) + right_side_regulation_before_turn, width = width).put(Bend_after_mmi['Bend_after_mmiR{}'.format(i)].pin['b0'])
            Bend_after_extenL['Bend_after_extenL{}'.format(i)] = nd.bend(radius= Bend_radius+dw*i , angle =-90, width = width).put(ext_after_bend['ext_after_bend_L{}'.format(i)].pin['b0'])
        
        
        
        
        strt_after_bendL = {}
        
        Bend_after_extenR = {}
        Bend_after_bendR = {}
        Bend_after_strtL = {}
        
        
        bend_after_strtL1 = {}
        strt_after_bendL1 = {}
        bend_after_strtL2 = {}
        strt_after_bendL2 = {}
        
        strt_after_bendL3 = {}
        strt_after_strtL3 = {}
        
        strt_after_bendR0 = {}
        bend_after_bendR1 = {}
        strt_after_bendR1 = {}
        bend_after_bendR2 = {}
        strt_after_bendR2 = {}
        
        for i in range(0,number//2):
            #####Below, this gives the length of the straight lines above our waveguides
            Test_length  = length+ell + 4*LegLength + 2*BodyLength + 2*offset + (number//2-1)*dw+dw + 2* Bend_radius+small_corecction#-width/2
            print(Test_length)
            #Prev_Length  = 3*number*dw+2*LegLength+2*BodyLength +2*offset+length
            strt_after_bendL['strt_after_bend_L{}'.format(i)] = nd.strt(length  = Test_length, width = width).put(Bend_after_extenL['Bend_after_extenL{}'.format(i)].pin['b0'])
            bend_after_strtL1["Bend_after_strt_L1{}".format(i)] = nd.bend(radius = Bend_radius+dw*i, angle = -90 , width = width).put(strt_after_bendL['strt_after_bend_L{}'.format(i)].pin['b0'])
            ######## Length of the straight connecting after the two length ################
            length_to_find_the_middle =  distance*dcm*((number-1)//2)+ distance +mass_turn 
            ltftm = length_to_find_the_middle
            ###########################################
            #strt_after_bendL1['strt_after_bendL1{}'.format(i)] = nd.strt(length = length_to_find_the_middle , width = width , layer = 400 ).put(bend_after_strtL1['Bend_after_strt_L1{}'.format(i)].pin['b0'])
    
            ################################################################################################################
            ###############################################################################################################
            Bend_after_extenR['Bend_after_extenR{}'.format(i)] = nd.bend(radius= Bend_radius+dw*i , angle =90, width = width).put(ext_after_bend['ext_after_bend_R{}'.format(i)].pin['b0'])
            Bend_after_bendR['Bend_after_bendR{}'.format(i)] = nd.bend(radius= Bend_radius+dw*i , angle =90, width = width).put(Bend_after_extenR['Bend_after_extenR{}'.format(i)].pin['b0'])
            ##### There is a straight part at the bottom of the Waveguide 
            strt_after_bendR0['strt_after_bendR0{}'.format(i)] = nd.strt(length  = aa+mass_turn , width = width).put(Bend_after_bendR['Bend_after_bendR{}'.format(i)].pin['b0'])
            ##################################################################################################################
        
        
            theta_angle_of_bendR2 = 90 - theta_angle_of_bendR1
            
            correction_term = 0
            if Bend_radius > 100 :
                correction_term = 2*(Bend_radius-100)
            
            ########## Looking for the length "ll" of the strt_after_bendR1. Optimize it accordin to the total length and the angles that we want
            inrad = pi/180
            RR = (number//2)*dw + Bend_radius  # this is the maximum radius of the "largest arc
            Omega = ltftm -bb - RR - aa -3*dw 
            bbb = sin(inrad*theta_angle_of_bendR1)*RR
            omega = inrad*((180-theta_angle_of_bendR2)/2)
            gamma = 90- ((180-theta_angle_of_bendR2)/2)
            gamma = gamma*inrad
            ddd = RR*cos(omega - gamma)*tan(gamma) # omega and gamma are the relevant angles of the secant of the circle in the bend_after_bendR2
            ll =(Omega - bbb - ddd)/cos(inrad*theta_angle_of_bendR1) + esa 
            print(ll)
            ccc = ll*cos(theta_angle_of_bendR1*inrad)
            
            if theta_angle_of_bendR1 == 0:
                lbe = 0
            else:
                x1= RR*sin(inrad* theta_angle_of_bendR2)
                lbe = (ll)*sin(inrad*theta_angle_of_bendR1)
                
                
                #lbe = length_before_end
        
            strt_after_bendL2['strt_after_bendL2{}'.format(i)] = nd.strt(length = bb , width = width  ).put(bend_after_strtL1['Bend_after_strt_L1{}'.format(i)].pin['b0'])
            bend_after_strtL2["Bend_after_strt_L1{}".format(i)] = nd.bend(radius = Bend_radius+dw*((number//2)-i), angle = 90 , width = width).put(strt_after_bendL2['strt_after_bendL2{}'.format(i)].pin['b0'])
            strt_after_bendL3['strt_after_bendL3{}'.format(i)] = nd.strt(length = lbe , width = width  ).put(bend_after_strtL2["Bend_after_strt_L1{}".format(i)].pin['b0'])
            strt_after_strtL3['strt_after_strtL3{}'.format(i)] = nd.strt(length  = last_extension  , width = width).put(strt_after_bendL3['strt_after_bendL3{}'.format(i)].pin['b0'])
            strt_after_strtL3['strt_after_strtL3{}'.format(i)].raise_pins(['b0'],['Output{}'.format(i)])
            
            bend_after_bendR1['bend_after_bendR1{}'.format(i)] = nd.bend(radius= Bend_radius+dw*((number//2)-i) , angle =  -theta_angle_of_bendR1 , width = width).put(strt_after_bendR0['strt_after_bendR0{}'.format(i)].pin['b0'])
            strt_after_bendR1['strt_after_bendR1{}'.format(i)] = nd.strt(length  = ll , width = width).put(bend_after_bendR1['bend_after_bendR1{}'.format(i)].pin['b0'])
            bend_after_bendR2['bend_after_bendR2{}'.format(i)] = nd.bend(radius= Bend_radius+dw*((number//2)-i) , angle = - theta_angle_of_bendR2 , width = width).put( strt_after_bendR1['strt_after_bendR1{}'.format(i)].pin['b0'])
            strt_after_bendR2['strt_after_bendR2{}'.format(i)] = nd.strt(length  = last_extension+ 0 , width = width).put(bend_after_bendR2['bend_after_bendR2{}'.format(i)].pin['b0'])
            
            #nd.Pin("Input{}".format(i)).put(strt_after_bendR2['strt_after_bendR2{}'.format(i)].pin('b0'))
            strt_after_bendR2['strt_after_bendR2{}'.format(i)].raise_pins(['b0'],['Input{}'.format(i)])
            
            #nd.put_stub()
    
    
    
    ######LOOPS ################################################################################
    ######LOOPS ################################################################################
    ######LOOPS ################################################################################
    ######LOOPS ################################################################################
    
        alignement_layer = 44
        
    # =============================================================================
    #     with nd.Cell(name = "Loop") as Loop_Bot:
    # =============================================================================
        arbitrary_length1  = 200
        arbitrary_length2  = arbitrary_length1 -dw
        Bend_radius_loops = Bend_radius 
        x ,y , a = Main_Structure.pin['Input{}'.format(number//2-1)].xya()
        loop_p1 = nd.strt(length  = - last_extension , width = width , layer  = alignement_layer).put(x ,y - dw)
        loop_p1.raise_pins(['a0'],["Loop input/output"])
        loop_p2 = nd.bend(radius = Bend_radius_loops , angle = -90,  width  = width, layer = alignement_layer).put(loop_p1.pin[("b0")], flop = True)
        loop_p3 = nd.strt(length  = arbitrary_length1, width = width, layer = alignement_layer).put(loop_p2.pin[("b0")])
        loop_p4 = nd.bend(radius = Bend_radius_loops , angle = 180,  width  = width, layer = alignement_layer).put(loop_p3.pin[("b0")])
        loop_p5 = nd.strt(length  = arbitrary_length2, width = width, layer = alignement_layer).put(loop_p4.pin[("b0")])
        loop_p6 = nd.bend(radius = Bend_radius_loops , angle = -90,  width  = width, layer = alignement_layer).put(loop_p5.pin[("b0")])
        loop_p7 = nd.strt(length  = last_extension - 2*Bend_radius_loops, width = width, layer = alignement_layer).put(loop_p6.pin[("b0")])
        loop_p7.raise_pins(['b0'],[" Bot Loop input/output"])
        #nd.put_stub()
        
        
        #Loop_Bot.put()
           
        arbitrary_length1  = 200
        arbitrary_length2  = arbitrary_length1 -dw
        Bend_radius_loops = Bend_radius
        x ,y , a = Main_Structure.pin['Output{}'.format(number//2-1)].xya()
        Tloop_p1 = nd.strt(length  = - last_extension , width = width , layer  = alignement_layer).put(x ,y + dw)
        Tloop_p1.raise_pins(['a0'],[" Top Loop input/output"])
        Tloop_p2 = nd.bend(radius = Bend_radius_loops , angle = 90,  width  = width, layer = alignement_layer).put(Tloop_p1.pin[("b0")], flop = True)
        Tloop_p3 = nd.strt(length  = arbitrary_length1, width = width, layer = alignement_layer).put(Tloop_p2.pin[("b0")])
        Tloop_p4 = nd.bend(radius = Bend_radius_loops , angle = -180,  width  = width, layer = alignement_layer).put(Tloop_p3.pin[("b0")])
        Tloop_p5 = nd.strt(length  = arbitrary_length2, width = width, layer = alignement_layer).put(Tloop_p4.pin[("b0")])
        Tloop_p6 = nd.bend(radius = Bend_radius_loops , angle = 90,  width  = width, layer = alignement_layer).put(Tloop_p5.pin[("b0")])
        Tloop_p7 = nd.strt(length  = last_extension - 2*Bend_radius_loops, width = width, layer = alignement_layer).put(Tloop_p6.pin[("b0")])
        Tloop_p7.raise_pins(['b0'],["Loop input/output"])
        #nd.put_stub()
    
    #Top_Loop.put()
            
    # =============================================================================
    #     with nd.Cell(name = "Middle Loop") as Mid_Loop:
    # =============================================================================
    # =============================================================================
    #         mid_length  = last_extension 
    #         mid_arbitrary_length1  = 200
    #         mid_arbotrary_length3 = 220
    #         arbitrary_length2  = arbitrary_length1 -dw
    #         
    #         x ,y , a = Main_Structure.pin['Input0'].xya()
    #         mloop1 = nd.strt(length  =  - mid_length, width = width, layer  = alignement_layer).put(x, y+dw)
    #         mloop1.raise_pins(['a0'],['Mid Loop input/output'])
    #         mloop2 = nd.bend(radius  = Bend_radius + (number//2+1)*dw, angle = - theta_angle_of_bendR2 , width  = width,  layer = alignement_layer).put(mloop1.pin['b0'], flop = True)
    #         mloop3 = nd.strt(length  = mid_arbotrary_length3, width = width , layer = alignement_layer).put(mloop2.pin['b0'])
    #         mloop4 = nd.bend(radius  = Bend_radius, angle =  -180+ theta_angle_of_bendR1 , width  = width,  layer = alignement_layer).put(mloop3.pin['b0'])
    #         
    #         small_piece = Bend_radius*tan(inrad*theta_angle_of_bendR1) #this is the piece below the inclide intersection
    #         xxx= sin(theta_angle_of_bendR1*inrad)*( Bend_radius + (number//2+1)*dw)
    #         lll =  Bend_radius + (number//2+1)*dw - xxx
    #         kl = lll - Bend_radius
    #         
    #         
    #         mloop5 = nd.strt(length  = (mid_arbotrary_length3-small_piece)*cos(inrad*theta_angle_of_bendR1), width = width , layer = alignement_layer).put(mloop4.pin['b0'])
    #         mloop6 = nd.strt(length  = kl+dw, width = width , layer = alignement_layer).put(mloop5.pin['b0'])
    #         mloop7 = nd.bend(radius  = Bend_radius, angle = -90 , width  = width,  layer = alignement_layer).put(mloop6.pin['b0'])
    #         mloop7.raise_pins(['b0'],["b7"])
    #         
    #         xy = sin(inrad*theta_angle_of_bendR1)*(mid_arbitrary_length1-small_piece)
    #         xxy = cos(theta_angle_of_bendR1*inrad)*( Bend_radius + (number//2+1)*dw)
    #         distance_last = Bend_radius + xy + xxy + last_extension +small_corecction
    #         
    #         
    #         
    #         
    #         mloop8 = nd.strt(length  = distance_last, width = width , layer = alignement_layer).put(mloop7.pin['b0'])
    #         nd.put_stub()
    # =============================================================================
        
        
        
        #Mid_Loop.put()
    return Main_Structure
    

nd.export_gds(filename=r'Modulator')