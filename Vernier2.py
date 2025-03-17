# -*- coding: utf-8 -*-
"""
Created on Wed Oct  5 15:03:26 2022
VERNIER MASUREMENT
@author: aliat
"""

import nazca as nd 
def my_vernier2(iii,jjj):
    rod_length = 12
    rod_width = 10
    number_of_rods = 30
    letter_height = 20
    dist_combs = 7
    
    
    vernier_1_layer_top = 2
    v1lt = vernier_1_layer_top
    
    vernier_1_layer_bot = 2
    v1lb = vernier_1_layer_bot
    
    
    
    HorVernCombTopRodDist= 20
    HorVernCombBotRodDist= 20-5/15
    
    VerVernCombTopRodDist= 20
    VerVernCombBotRodDist= 19
    
    distnace_of_top_bot_combs_horiz = -9
    distnace_of_left_right_combs_ver = -3
    
    
    x_correction_vert_letters = -5
    y_correction_vert_letters = -2
    x_correction_horiz_letters = -3 ########
    y_correction_horiz_letters = -3
    
    
    with nd.Cell(name = "Vernier111112222") as VernierHorizontal:
        if (iii%2==0 and jjj%2==0) or (iii%2!=0 and jjj%2!=0):
    
            with nd.Cell(name = "HorVernTop44566543455") as HorVernTop:
                with nd.Cell(name = "SeedComb2top56677788") as SeedComb2top:
                    for i in range(0,3):
                        if i==1:
                            nd.strt(length = rod_length, width = rod_width- i*0.3*rod_width, layer = v1lt).put()
                        else:
                            nd.strt(length = rod_length, width = rod_width, layer = v1lt).put()
        
                SeedComb2top.put(0,0,-90)
                #nd.text("0", height=(letter_height)).put(x_correction_horiz_letters,0)
                for i in range(1,number_of_rods//2+1):
                    SeedComb2top.put(-HorVernCombTopRodDist*i,0,-90)
                    #nd.text("-{}".format(i), height=(letter_height)).put(-HorVernCombTopRodDist*i+3*x_correction_horiz_letters,0)
                    SeedComb2top.put(HorVernCombTopRodDist*i,0,-90)
                    #nd.text("{}".format(i), height=(letter_height)).put(HorVernCombTopRodDist*i+x_correction_horiz_letters,0)
        
            HorVernTop.put(0,0)
        else:
            with nd.Cell(name = "HorVernBot3345566") as HorVernBot:
                with nd.Cell(name = "SeedComb2Bot1234455") as SeedComb2Bot:
        
                    nd.strt(length = 3*rod_length, width = rod_width, layer = v1lb).put()
                SeedComb2Bot.put(0,0,-90)
                nd.text("0", height=(letter_height), layer = 2).put(x_correction_horiz_letters,-3.2*rod_length+dist_combs-9-25)
                for i in range(1,number_of_rods//2+1):
                    SeedComb2Bot.put(-HorVernCombBotRodDist*i,0,-90)
                    if i%2!=0:
                        nd.text("-{}".format(i), height=(letter_height), layer = 2).put(-HorVernCombBotRodDist*i+x_correction_horiz_letters,-3.2*rod_length+dist_combs-9-33, 45)
                    SeedComb2Bot.put(HorVernCombBotRodDist*i,0,-90)
                    if i%2!=0:
                        nd.text("{}".format(i),height=(letter_height), layer = 2).put(HorVernCombBotRodDist*i+x_correction_horiz_letters+10,-3.2*rod_length+dist_combs-9 -30, 45)
            HorVernBot.put(0,-3*rod_length-dist_combs-distnace_of_top_bot_combs_horiz)
            nd.text("y", height=(100), layer = 2).put(-305,-3*rod_length-dist_combs-distnace_of_top_bot_combs_horiz+45)
                
    VernierHorizontal.put(2300+430,-1900-330,-90)




