# -*- coding: utf-8 -*-
"""
Created on Mon Jan 30 10:55:49 2023
This a code to replace all the save directories from the previous directory which is Users/alia/One... to users/alexa
@author: alexa
"""


import os 

from os.path import join,getsize 


i = 0
for root, dirs, files in os.walk(r"C:\Users\alexa\Desktop\APD Mask V5"):
# =============================================================================
#     print(len(files))
#     print(files)
# =============================================================================
    for i in range(len(files)):
        print(files[i])
        print("\n")

    for i in range(len(files)):
        fin  = open("{}".format(files[i]),"rt")
        data = fin.read()
        print(data)
        print("\n")
        data = data.replace("alexa", "alexa")
        fin.close()
        
        fin = open("{}".format(files[i]), "wt")
        fin.write(data)
        fin.close

    
    

