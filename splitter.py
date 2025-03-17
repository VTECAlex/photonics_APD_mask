import nazca as nd
import nazca.demofab as demo

def mmi(offset=40):
    with nd.Cell(name='myMMI') as mymmi:
        mmi1 = demo.mmi1x2_sh().put(100,100)
        elm1 = demo.shallow.strt(length=100).put(mmi1.pin['a0'])
        elm2 = demo.shallow.sbend(offset=offset).put(mmi1.pin['b0'])
        elm3 = demo.shallow.sbend(offset=-offset).put(mmi1.pin['b1'])

        nd.Pin('a0', pin=elm1.pin['b0']).put()
        nd.Pin('b0', pin=elm2.pin['b0']).put()
        nd.Pin('b1', pin=elm3.pin['b0']).put()
    return mymmi

with nd.Cell(name='splitter') as splitter_1x8:
    mmi1  = mmi(offset=100).put()
    mmi2a = mmi(offset=50).put(mmi1.pin['b0'])
    mmi2b = mmi(offset=50).put(mmi1.pin['b1'])
    mmi3a = mmi(offset=25).put(mmi2a.pin['b0'])
    mmi3b = mmi(offset=25).put(mmi2a.pin['b1'])
    mmi3c = mmi(offset=25).put(mmi2b.pin['b0'])
    mmi3d = mmi(offset=25).put(mmi2b.pin['b1'])
    
    nd.Pin('a0', pin=mmi1.pin['a0']).put()
    nd.Pin('b0', pin=mmi3a.pin['b0']).put()
    nd.Pin('b1', pin=mmi3a.pin['b1']).put()
    nd.Pin('b2', pin=mmi3b.pin['b0']).put()
    nd.Pin('b3', pin=mmi3b.pin['b1']).put()
    nd.Pin('b4', pin=mmi3c.pin['b0']).put()
    nd.Pin('b5', pin=mmi3c.pin['b1']).put()
    nd.Pin('b6', pin=mmi3d.pin['b0']).put()
    nd.Pin('b7', pin=mmi3d.pin['b1']).put()
    
split1x8 = splitter_1x8.put(0)
demo.shallow.strt(length=200).put(split1x8.pin['b4'])


nd.export_gds(filename='parametrizedbuildingblocks.gds')