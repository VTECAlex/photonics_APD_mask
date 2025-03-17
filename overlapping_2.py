from math import *


r = 10
d = 0

overlap_area = (1/2) * ((acos(d/(2*r)))**2) * r - ((d*r)/2) * sqrt(1-((d**2)/(4*r**2)))

print(overlap_area)




overlap_area_1 = 2*(r**2)*(acos(d/(2*r)))-(1/2)*d*sqrt(4*r**2-d**2)
print((overlap_area_1/(pi*r**2))*100)