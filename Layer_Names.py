import nazca as nd

import csv
import pandas as pd




def vbb_layers(name):
    df = pd.read_csv("EBL_Mask_Layers.csv")

    index = 1
    not_found = True
    while not_found == True:
        name_in_list = df.loc[index, "layer_name"]
        if name_in_list.lower() == name.lower():
            not_found = False
        elif index > df["layer_name"].shape[0]:
            print("The layer hasn't been found.")
            index = 0
            break
        else:
            index+=1

    return index
    



