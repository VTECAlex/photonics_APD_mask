import nazca as nd
import nazca.geometries as geom
#import Reticle1
import doted_circle
#import Dotted_circle
# Wafer Size
size_of_wafer  = 4
sow = size_of_wafer*2.54*10000

#
diameter_of_wafer= sow
radius_of_wafer  = diameter_of_wafer/2
# wafer = nd.Polygon(layer=1, points=geom.circle(radius=sow, N = 600)).put(0,0)


starting_length = 10
increasing_step = 0
number_of_grating = 50
grating_pitch = 0.4
grating_width = 0.25
diameter_of_wafer = 3000  # Assuming a diameter for the wafer

with nd.Cell(name="asdf1") as asdf1:
    for i in range(number_of_grating + 1):
        nd.strt(layer=2, length=grating_width, width=starting_length + i * increasing_step).put(i * grating_pitch + grating_width, 0)
        nd.strt(length=300, width=10).put(500, 0)

    # Define the coordinates for the trapezium points
    point1 = (500, starting_length / 10)
    point2 = ((number_of_grating + 0) * grating_pitch + grating_width, starting_length / 2 + number_of_grating * increasing_step / 2)
    point3 = (101, -starting_length / 2)
    point4 = (500, -starting_length / 10)  # Additional point to create a trapezium

    # Create the trapezium using nd.Polygon
    #nd.Polygon(layer=33, points=[point1, point2, point3, point4]).put(0, 0)

# Placing instances of 'asdf1' cell
for i in range(0, 8):
    for j in range(8):
        asdf1.put(i * -2000, j * 3000)
        asdf1.put(i * 2000, j * 3000)
        asdf1.put(i * 2000, j * -3000)
        asdf1.put(i * -2000, j * -3000)
nd.export_gds(filename="Grating_V1.gds")