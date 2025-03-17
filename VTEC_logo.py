import nazca as nd




def VTEC_Logo(layer,posx,posy):
    with nd.Cell('VTEC Logo:{},{}'.format(posx,posy)) as vtec_logo:
        [nd.text('V  T  E  C', height=100, align='rb', layer=layer).put(95, 0)
         for layer in [layer]]
        [nd.text('LASERS & SENSORS', height=50, align='rb', layer=layer).put(120, -50)
         for layer in [layer]]
        outline = [(0, 0), (0, 10), (8.7, 15), (8.7, 25), (17.4, 30), (0, 40), (-17.4, 30), (-17.4, 10), (0, 0),
                   (0, 10),
                   (-8.7, 15), (-8.7, 25), (0, 30), (8.7, 25), (8.7, 15), (0, 10), (-8.7, 15), (0, 20), (0, 30),
                   (8.7, 25),
                   (8.7, 15), (0, 10)]
        nd.Polygon(layer=layer, points=outline).put(-450, -50, scale=4)
    return vtec_logo
# VTEC_Logo(2,0,0).put()
# nd.export_gds(filename='VTEC_Logo.gds')