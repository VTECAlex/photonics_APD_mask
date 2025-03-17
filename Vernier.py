# -*- coding: utf-8 -*-
"""
Created on Wed Oct  5 15:03:26 2022
VERNIER MASUREMENT
@author: aliat
"""

import nazca as nd 

rod_length = 12
rod_width = 10
number_of_rods = 30
letter_height = 3
dist_combs = 7


HorVernCombTopRodDist= 20
HorVernCombBotRodDist= 19

VerVernCombTopRodDist= 20
VerVernCombBotRodDist= 19

distnace_of_top_bot_combs_horiz = -9
distnace_of_left_right_combs_ver = -3


x_correction_vert_letters = -5
y_correction_vert_letters = -2
x_correction_horiz_letters = -1
y_correction_horiz_letters = -3


with nd.Cell(name = "Vernier111112222") as VernierHorizontal:

    with nd.Cell(name = "HorVernTop44566543455") as HorVernTop:
        with nd.Cell(name = "SeedComb2top56677788") as SeedComb2top:
            for i in range(0,3):
                if i==1:
                    nd.strt(length = rod_length, width = rod_width- i*0.3*rod_width, layer = 11).put()
                else:
                    nd.strt(length = rod_length, width = rod_width, layer = 11).put()

        SeedComb2top.put(0,0,-90)
        nd.text("0", height=(letter_height), layer = 11).put(x_correction_horiz_letters,0)
        for i in range(1,number_of_rods//2+1):
            SeedComb2top.put(-HorVernCombTopRodDist*i,0,-90)
            nd.text("-{}".format(i), height=(letter_height), layer = 11).put(-HorVernCombTopRodDist*i+3*x_correction_horiz_letters,0)
            SeedComb2top.put(HorVernCombTopRodDist*i,0,-90)
            nd.text("{}".format(i), height=(letter_height), layer = 11).put(HorVernCombTopRodDist*i+x_correction_horiz_letters,0)

    HorVernTop.put(0,0)
    
    with nd.Cell(name = "HorVernBot3345566") as HorVernBot:
        with nd.Cell(name = "SeedComb2Bot1234455") as SeedComb2Bot:

            nd.strt(length = 3*rod_length, width = rod_width, layer = 11).put()
        SeedComb2Bot.put(0,0,-90)
        nd.text("0", height=(letter_height), layer = 11).put(x_correction_horiz_letters,-3.2*rod_length+dist_combs-9)
        for i in range(1,number_of_rods//2+1):
            SeedComb2Bot.put(-HorVernCombBotRodDist*i,0,-90)
            nd.text("-{}".format(i), height=(letter_height), layer = 11).put(-HorVernCombBotRodDist*i+x_correction_horiz_letters,-3.2*rod_length+dist_combs-9)
            SeedComb2Bot.put(HorVernCombBotRodDist*i,0,-90)
            nd.text("{}".format(i),height=(letter_height), layer = 11).put(HorVernCombBotRodDist*i+x_correction_horiz_letters,-3.2*rod_length+dist_combs-9)
    HorVernBot.put(0,-3*rod_length-dist_combs-distnace_of_top_bot_combs_horiz)
            
VernierHorizontal.put(-1000,-1000)


#==============================================================================

with nd.Cell(name = "Vernier22233322") as VernierVertical:

    
    with nd.Cell(name = "VerVernTop45334555") as VerVernLeft:
        with nd.Cell(name = "SeedComb1top54353456") as SeedCombLeft:
            for i in range(0,3):
                if i==1:
                    nd.strt(length = rod_length, width = rod_width- i*0.3*rod_width, layer = 11).put()
                else:
                    nd.strt(length = rod_length, width = rod_width, layer = 11).put()

        SeedCombLeft.put(0,0)
        nd.text("0", height=(letter_height), layer = 11).put(x_correction_vert_letters, y_correction_vert_letters)
        for i in range(1,number_of_rods//2+1):
            SeedCombLeft.put(0,-VerVernCombTopRodDist*i)
            nd.text("-{}".format(i), height=(letter_height), layer = 11).put(1.5*x_correction_vert_letters,-VerVernCombTopRodDist*i+y_correction_vert_letters)
            SeedComb2top.put(0,VerVernCombTopRodDist*i)
            nd.text("{}".format(i), height=(letter_height), layer = 11).put(x_correction_vert_letters,VerVernCombTopRodDist*i+y_correction_vert_letters)

    VerVernLeft.put(0,0)
    
    with nd.Cell(name = "VerVernBot2123123") as VerVernRight:
        with nd.Cell(name = "SeedComb1Bot4234453") as SeedCombRight:
            nd.strt(length = 3*rod_length, width = rod_width, layer = 11).put()
        SeedCombRight.put(0,0)
        nd.text("0", height=(letter_height), layer = 11).put(3*rod_length+dist_combs,y_correction_vert_letters)
        for i in range(1,number_of_rods//2+1):
            SeedComb2Bot.put(0,-VerVernCombBotRodDist*i)
            nd.text("-{}".format(i), height=(letter_height), layer = 11).put(3*rod_length+dist_combs,-VerVernCombBotRodDist*i+y_correction_vert_letters)
            SeedComb2Bot.put(0,VerVernCombBotRodDist*i)
            nd.text("{}".format(i),height=(letter_height), layer = 11).put(3*rod_length+dist_combs,VerVernCombBotRodDist*i+y_correction_vert_letters)
    VerVernRight.put(3*rod_length+distnace_of_left_right_combs_ver,0)
            
VernierVertical.put(0,10000)












nd.export_gds(filename='VernierTest.gds')
                

