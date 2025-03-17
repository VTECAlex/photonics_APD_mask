import math


x1 = 0
y1 = 0
y2 = 0

x2 = 10
r1 = 10
r2 = r1
# Calculate the distance between the centers of the circles
distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Check if the circles are separate
if distance >= r1 + r2:
    print("no overlap")

# Check if one circle is completely inside the other
elif distance <= abs(r1 - r2):
    print("100% overlap")

else:
    # Calculate the area of intersection using the formula for the area of a lens
    angle1 = 2 * math.acos((r1**2 + distance**2 - r2**2) / (2 * r1 * distance))
    angle2 = 2 * math.acos((r2**2 + distance**2 - r1**2) / (2 * r2 * distance))
    area_of_intersection = 0.5 * (r1**2 * (angle1 - math.sin(angle1)) + r2**2 * (angle2 - math.sin(angle2)))

    # Calculate the total area of the two circles
    area_of_circle1 = math.pi * r1**2
    area_of_circle2 = math.pi * r2**2

    # Calculate the overlap percentage
    overlap_percentage = (area_of_intersection / (area_of_circle1 + area_of_circle2 - area_of_intersection)) * 100


print(overlap_percentage)







