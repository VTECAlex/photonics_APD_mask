# -*- coding: utf-8 -*-
"""
Created on Tue Nov  7 09:10:10 2023

@author: alexa
"""

import math

def calculate_circle_overlap(center1, radius1, center2, radius2):
    # Calculate the distance between the two circle centers
    distance = math.sqrt((center2[0] - center1[0])**2 + (center2[1] - center1[1])**2)
    
    # Check if the circles do not overlap at all
    if distance >= radius1 + radius2:
        return 0.0
    
    # Check if one circle is completely contained within the other
    if distance <= abs(radius1 - radius2):
        return 1.0
    
    # Calculate the areas of the two circles
    area1 = math.pi * radius1**2
    area2 = math.pi * radius2**2
    
    # Calculate the angle and area of the intersection sector
    angle1 = 2 * math.acos((radius1**2 + distance**2 - radius2**2) / (2 * radius1 * distance))
    area_sector1 = 0.5 * radius1**2 * (angle1 - math.sin(angle1))
    
    # Calculate the angle and area of the intersection sector for the second circle
    angle2 = 2 * math.acos((radius2**2 + distance**2 - radius1**2) / (2 * radius2 * distance))
    area_sector2 = 0.5 * radius2**2 * (angle2 - math.sin(angle2))
    
    # Calculate the total area of the intersection
    intersection_area = area_sector1 + area_sector2
    
    # Calculate the percentage overlap
    overlap_percentage = (intersection_area / min(area1, area2)) * 100.0
    
    return overlap_percentage

# Example usage
diameter = 18
r = diameter/2
bss = 10
d = bss

center1 = (0, 0)
radius1 = r
center2 = (bss, 0)
radius2 = radius1
percentage_overlap = calculate_circle_overlap(center1, radius1, center2, radius2)
print(f"Method 1: Percentage overlap: {percentage_overlap}%")

print("-"*80)

# print("overlap", 2*[(r**2)*((math.cos(d/(2*r)))**(-1))-(d/4)*math.sqrt(4*r**2-d**2)/(math.pi*r**2)])

print("-"*80)
overlap_area_1 = 2*(r**2)*(math.acos(d/(2*r)))-(1/2)*d*math.sqrt(4*r**2-d**2)
print("Method 2: Percentage overlap : ", (overlap_area_1/(math.pi*r**2))*100)


