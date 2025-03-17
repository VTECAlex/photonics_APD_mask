# -*- coding: utf-8 -*-
"""
Created on Wed Oct  5 15:03:26 2022
VERNIER MASUREMENT
@author: aliat
"""

import nazca as nd 

def TVFG3(iii,jjj):


    grod_length = 100
    grod_width = 20
    gnumber_of_rods = 12
    gletter_height = 3
    gdist_combs = 10 - 180
    
    
    gHorVernCombTopRodDist= 80
    gHorVernCombBotRodDist= 80-0.5
    
    gVerVernCombTopRodDist= gHorVernCombTopRodDist
    gVerVernCombBotRodDist= gVerVernCombTopRodDist
    
    gdistnace_of_top_bot_combs_horiz = -30
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
                        nd.strt(length = grod_length, width = gr_rod_width, layer = 50).put()
                with nd.Cell(name = "SeedComb2top") as SeedComb2topMid:
                    for i in range(0,3):
                        gr_rod_width = grod_width*((1/2)**i)
                        nd.strt(length = grod_length+0.4*grod_length, width = gr_rod_width, layer = 50).put()
        
        
                SeedComb2topMid.put(0,0,-90)
                #nd.text("0", height=(letter_height)).put(x_correction_horiz_letters,0)
                for i in range(1,gnumber_of_rods//2+1):
                    SeedComb2topGeert.put(-gHorVernCombTopRodDist*i,0,-90)
                    #nd.text("-{}".format(i), height=(letter_height)).put(-HorVernCombTopRodDist*i+3*x_correction_horiz_letters,0)
                    SeedComb2topGeert.put(gHorVernCombTopRodDist*i,0,-90)
                    #nd.text("{}".format(i), height=(letter_height)).put(HorVernCombTopRodDist*i+x_correction_horiz_letters,0)
            nd.text("y 0.5", height=(30)).put(0+30,0)
            HorVernTopGeert.put(0,0)
        else:
    
    
            with nd.Cell(name = "HorVernBot") as gHorVernBotGeert:
                with nd.Cell(name = "SeedComb2Bot") as SeedComb2BotGeert:
        
                    nd.strt(length = 3*grod_length, width = grod_width, layer = 40).put()
                #SeedComb2Bot.put(0,0,-90)
                nd.text("0", height=(gletter_height)).put(gx_correction_horiz_letters,-3.2*grod_length+gdist_combs)
                for i in range(1,gnumber_of_rods//2+1):
                    SeedComb2BotGeert.put(-gHorVernCombBotRodDist*i+gHorVernCombTopRodDist/2,0,-90)
                    nd.text("-{}".format(i), height=(gletter_height)).put(-gHorVernCombBotRodDist*i+gx_correction_horiz_letters+gHorVernCombTopRodDist/2,-3.2*grod_length+gdist_combs)
                    SeedComb2BotGeert.put(gHorVernCombBotRodDist*i-gHorVernCombTopRodDist/2,0,-90)
                    nd.text("{}".format(i),height=(gletter_height)).put(gHorVernCombBotRodDist*i+gx_correction_horiz_letters-gHorVernCombTopRodDist/2,-3.2*grod_length+gdist_combs)
            gHorVernBotGeert.put(0,-3*grod_length-gdist_combs-gdistnace_of_top_bot_combs_horiz)
    
    #nd.text("y 0.5", height=(30)).put(1100-15,1800)
        nd.text("y 0.5", height=(30)).put(0+30,0)
    return gVernierHorizontalGeert.put(2300,1350,-90)
            
            #==============================================================================
# =============================================================================
# def TVFG2(iii):
#     grod_length = 100
#     grod_width = 20
#     gnumber_of_rods = 12
#     gletter_height = 3
#     gdist_combs = 10
#     
#     
#     gHorVernCombTopRodDist= 80
#     gHorVernCombBotRodDist= gHorVernCombTopRodDist
#     
#     gVerVernCombTopRodDist= gHorVernCombTopRodDist
#     gVerVernCombBotRodDist= gVerVernCombTopRodDist
#     
#     gdistnace_of_top_bot_combs_horiz = -30
#     gdistnace_of_left_right_combs_ver = -3
#     
#     
#     gx_correction_vert_letters = -3
#     gy_correction_vert_letters = -2
#     gx_correction_horiz_letters = -1
#     with nd.Cell(name = "Vernier") as gVernierVerticalGeert:
#         if iii%2==0:
#             
#             with nd.Cell(name = "VerVernTop") as VerVernLeftGeert:
#                 with nd.Cell(name = "SeedComb1top") as SeedCombLeftGeert:
#                     gr_rod_width = grod_width
#         
#                     for i in range(0,3):
#                         if i==1:
#                             gr_rod_width = grod_width*((1/2)**i)
#         
#                             nd.strt(length = grod_length, width = gr_rod_width, layer = 50).put()
#                             
#                 with nd.Cell(name = "SeedComb1top") as SeedCombLeftMid:
#                     gr_rod_width = grod_width
#         
#                     for i in range(0,3):
#                         if i==1:
#                             gr_rod_width = grod_width*((1/2)**i)
#         
#                             nd.strt(length = grod_length+0.4*grod_length, width = gr_rod_width, layer = 50).put()
#                             
#                 
#                 
#         
#         
#                 SeedCombLeftMid.put(0,0)
#                 nd.text("0", height=(gletter_height)).put(gx_correction_vert_letters, gy_correction_vert_letters)
#                 for i in range(1,gnumber_of_rods//2+1):
#                     SeedCombLeftGeert.put(0,-gVerVernCombTopRodDist*i)
#                     #nd.text("-{}".format(i), height=(letter_height)).put(1.5*x_correction_vert_letters,-VerVernCombTopRodDist*i+y_correction_vert_letters)
#                     SeedCombLeftGeert.put(0,gVerVernCombTopRodDist*i)
#                     #nd.text("{}".format(i), height=(letter_height)).put(x_correction_vert_letters,VerVernCombTopRodDist*i+y_correction_vert_letters)
#         
#             VerVernLeftGeert.put(0,0)
#         else:
#             
#             with nd.Cell(name = "VerVernBot") as gVerVernRightGeert:
#                 with nd.Cell(name = "SeedComb1Bot") as SeedCombRight:
#                     nd.strt(length = 3*grod_length, width = grod_width, layer = 40).put()
#                 #SeedCombRight.put(0,0)
#                 #nd.text("0", height=(letter_height)).put(3*rod_length+dist_combs,y_correction_vert_letters)
#                 for i in range(1,gnumber_of_rods//2+1):
#                     SeedCombRight.put(0,-gVerVernCombBotRodDist*i+gVerVernCombTopRodDist/2)
#                     #nd.text("-{}".format(i), height=(letter_height)).put(3*rod_length+dist_combs,-VerVernCombBotRodDist*i+y_correction_vert_letters+VerVernCombTopRodDist/2)
#                     SeedCombRight.put(0,gVerVernCombBotRodDist*i-gVerVernCombTopRodDist/2)
#                     #nd.text("{}".format(i),height=(letter_height)).put(3*rod_length+dist_combs,VerVernCombBotRodDist*i+y_correction_vert_letters+VerVernCombTopRodDist/2)
#             gVerVernRightGeert.put(3*grod_length+gdistnace_of_left_right_combs_ver,0)
#                 
#     gVernierVerticalGeert.put(2100,1350)
# =============================================================================









TVFG3(2,4)


nd.export_gds(filename='VernierTestGeert.gds')
                

