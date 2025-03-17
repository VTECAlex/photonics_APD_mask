import nazca as nd
import Frame_for_tile

with nd.Cell(name="Test Lines") as Test_lines:
    for i in range(5):
        nd.strt(width=5 + i * 5, length=2000, layer="EBL_Tile_Bars").put(0, -i * 100)
        nd.text("{}".format(5 + i * 5)).put(-70, -i * 100)
Test_lines.put(0, 0)
Test_lines.put(-1000, 0, 90)







nd.export_gds(filename=r'EBL_MapV1_DT_Lines')

