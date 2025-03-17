# -*- coding: utf-8 -*-
"""
Created on Thu Nov 17 15:16:47 2022

@author: aliat
"""

import nazca as nd




def invert_text(cell, layer1, layer2):
    lay1 = []
    lay2 = []
    layer1 = nd.get_layer(layer1)
    layer2 = nd.get_layer(layer2)
    for pgon in cell.polygons:
        node, Poly = pgon
        x0, y0, _ = node.xya()
        if Poly.layer == layer1:
            lay1.append([[x + x0, y + y0] for x, y in Poly.points])
        elif Poly.layer == layer2:
            lay2.append([[x + x0, y + y0] for x, y in Poly.points])
    with nd.Cell("newtxt") as newtxt:
        inverse = nd.clipper.diff_polygons(lay2, lay1)
        for pol in inverse:
            nd.Polygon(points=pol, layer=layer2).put()
    return newtxt