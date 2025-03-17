# -*- coding: utf-8 -*-
"""
Created on Wed Oct  5 15:03:26 2022
VERNIER MASUREMENT
@author: aliat
"""

import nazca as nd 

def TVFG1(iii,jjj):
# =============================================================================
#     iii = iii + 4
#     jjj = jjj + 3
# =============================================================================

    grod_length = 100
    grod_width = 20
    gnumber_of_rods = 12
    gletter_height = 3
    gdist_combs = 10-180
    
    vernier_1_layer_top = 2
    v1lt = vernier_1_layer_top
    
    vernier_1_layer_bot = 2
    v1lb = vernier_1_layer_bot
    
    
    gHorVernCombTopRodDist= 40
    gHorVernCombBotRodDist= 40-0.5
    
    gVerVernCombTopRodDist= gHorVernCombTopRodDist
    gVerVernCombBotRodDist= gVerVernCombTopRodDist
    
    gdistnace_of_top_bot_combs_horiz = -80
    gdistnace_of_left_right_combs_ver = -3
    
    
    gx_correction_vert_letters = -3
    gy_correction_vert_letters = -2
    gx_correction_horiz_letters = -1
    
    
    
    with nd.Cell(name = "Vernier") as gVernierHorizontalGeert:

        if (iii%2==0 and jjj%2==0) or (iii%2!=0 and jjj%2!=0):
            with nd.Cell(name = "HorVernTop") as HorVernTopGeert:
                gr_rod_width = grod_width
        
                with nd.Cell(name = "SeedComb2top") as SeedComb2topGeert:
                    for i in range(0,3):
                        gr_rod_width = grod_width*((1/2)**i)
                        nd.strt(length = grod_length, width = gr_rod_width, layer = v1lt).put()
                with nd.Cell(name = "SeedComb2top") as SeedComb2topMid:
                    for i in range(0,3):
                        gr_rod_width = grod_width*((1/2)**i)
                        nd.strt(length = grod_length+0.4*grod_length, width = gr_rod_width, layer = v1lt).put()
        
        
                SeedComb2topMid.put(0,0,-90)
                
                for i in range(1,(gnumber_of_rods-1)//2+1):
                    SeedComb2topGeert.put(-gHorVernCombTopRodDist*i,0,-90)
                    
                    SeedComb2topGeert.put(gHorVernCombTopRodDist*i,0,-90)
                    
        
            HorVernTopGeert.put(0,0)
        else:
    
    
            with nd.Cell(name = "HorVernBot") as gHorVernBotGeert:
                with nd.Cell(name = "SeedComb2Bot") as SeedComb2BotGeert:
        
                    nd.strt(length = 3*grod_length, width = grod_width, layer = v1lb).put()
                #SeedComb2Bot.put(0,0,-90)
                #nd.text("0", height=(gletter_height)).put(gx_correction_horiz_letters,-3.2*grod_length+gdist_combs)
                for i in range(1,gnumber_of_rods//2+1):
                    SeedComb2BotGeert.put(-gHorVernCombBotRodDist*i-0.5/2+gHorVernCombTopRodDist/2,0,-90)
                    #nd.text("-{}".format(i), height=(gletter_height)).put(-gHorVernCombBotRodDist*i+gx_correction_horiz_letters+gHorVernCombTopRodDist/2,-3.2*grod_length+gdist_combs)
                    SeedComb2BotGeert.put(gHorVernCombBotRodDist*i+0.5/2-gHorVernCombTopRodDist/2,0,-90)
                    #nd.text("{}".format(i),height=(gletter_height)).put(gHorVernCombBotRodDist*i+gx_correction_horiz_letters-gHorVernCombTopRodDist/2,-3.2*grod_length+gdist_combs)
            gHorVernBotGeert.put(0,-3*grod_length-gdist_combs-gdistnace_of_top_bot_combs_horiz)
            nd.text("x", height=(200),layer=2).put(1100-15+300-900-213-4.75,1800-60-1900-7)
            nd.text("0.5", height=(200), layer = 2).put(1100-15+300-900-213-4.75-280-110,1800-60-1900-7-431)
    return gVernierHorizontalGeert.put(1100+870+430-270,1800+950)




TVFG1(2,4)







nd.export_gds(filename='VernierTestGeert.gds')
                

