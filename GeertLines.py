# -*- coding: utf-8 -*-
"""
Created on Tue Oct 18 17:14:32 2022
Geett LINES
@author: aliat
"""

import nazca as nd

with nd.Cell(name  = "Geert_Lines") as Geert_Lines:
   pos = 0.25
   kj = 0
   for j in range(0,10):
       with nd.Cell(name = "Bundle of lines") as BundleLines:
           thickness  =  9*(1.5+j*0.5)
           
           nd.strt(length = thickness, width = 20, layer = 2).put(pos, 50+4*(1+6*0.5)/2 +2+200)
           nd.strt(length = 9*(1.5+j*0.5), width = 20, layer = 2).put(pos, -(50+4*(1+6*0.5)/2)-2-200)
           for i in range(0,5):
               
               nd.strt(length  = 1.5+j*0.5, width = 500, layer = 2).put(2*i*((1.5+j*0.5))+pos,0)
               line_thickness = 1.5+j*0.5 
           pos = pos + line_thickness*10+10+0.25


       BundleLines.put()
       
       
       
        
         
Geert_Lines.put(0,0)     
         
nd.export_gds(filename='GeertLines.gds')