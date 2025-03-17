



import nazca as nd


# def Onegrating(i)

with nd.Cell(name = 'Please kill me now') as yes_please:
    for i in range(0,90,-1):
        with nd.Cell(name = "One gret6ting") as onegrating:
                pitch = 0.8
                width = 0.6*0.8
                nd.bend(radius = 400+i*pitch, width  = width , angle = 30, layer = 10).put(0,-400+i*pitch)

        onegrating.put(0,0,0)



yes_please.put()

nd.export_gds(filename=r'Krishnaaaaaaa')