# -*- coding: utf-8 -*-
"""
Created on Mon Feb 20 15:13:57 2023

@author: alexa
"""

import nazca as nd



#varion in width
#variation in length 

with nd.Cell(name = "Matrix of bars") as matrix_of_bars:
    for j in range(0,3):
        with nd.Cell(name = "test cell") as test_cell:
            test_width  = 5
            distance  =  100*(j+1)
            width_of_metal_pad = 100
            length_of_metal_pad = 100
            layer = 2
            with nd.Cell(name="Metal pad") as metal_pad:
                nd.strt(width= width_of_metal_pad , length  = length_of_metal_pad , layer = layer).put()
                
            with nd.Cell(name = "Clumn of bars") as Column_of_bars:
                
                number_of_bars_variation_in_width = 4
                nobviw = number_of_bars_variation_in_width 
                wwv= [5,10,20,50]
                for i in range(nobviw):
                    yy = (200+width_of_metal_pad)*i
                    
                    nd.text("{},{}".format(wwv[i], distance), layer = layer).put(0, yy+50,0)

                    metal_pad.put(-length_of_metal_pad  , yy )
                    metal_pad.put(distance, yy )
                    nd.strt(width = wwv[i], length  = distance , layer = layer).put(0, yy )
            Column_of_bars.put()
        test_cell.put(100*(j+1)+600*j,0)
        
matrix_of_bars.put()


nd.export_gds(filename='Bars and Pads.gds')


