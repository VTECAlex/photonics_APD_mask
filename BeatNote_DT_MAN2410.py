from Pattern_Map_EBL_V2 import *
import nazca as nd
from VTEC_logo import *
import WVG as wvg

# nd.add_layer(name = "AM", layer = 1)
# nd.add_layer(name = "DA", layer = 2)
# nd.add_layer(name = "Logo", layer = 3)

EBL_Map_V2(222,2222).put(0,0)
VTEC_Logo(3333).put(0,2410-100)
wvg.waveguides().put(-1789+326.41/2,-4720+3474-1199.125/2)




nd.export_gds(filename='BeatNote_DT_MAN2410.gds')
