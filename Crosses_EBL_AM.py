import nazca as nd
from collections import defaultdict



def merge_polygons(cell, layers):
    """Merge all polygons per layer after flattening <cell>.

    Cell <cell> itself will not be affected. Note that a merged polygons may
    still consist of multiple polygons (islands).

    Args:
        cell (Cell): cell to process
        layers (list of str): names of layers to merge polygons in

    Returns:
        dict: {layer_name: merged_polygon}
    """
    pgons = defaultdict(list)
    for params in nd.cell_iter(cell, flat=True):
        for pgon, xy, bbox in params.iters['polygon']:
            for lay in layers:
                if pgon.layer == lay:
                    pgons[lay].append(xy)
    for lay in layers:
        pgons[lay] = nd.clipper.merge_polygons(pgons[lay])
    return pgons


def remove_polygons(cell, layers):
    """Remove all polygons in <layers> from <cell>.

    Args:
        cell (Cell): cell to process
        layers (list of str): names of layers to delete polygons from

    Returns:
        None
    """
    for params in nd.cell_iter(cell):
        if params.cell_start:
            pgons = []
            for pgon in params.cell.polygons:
                if pgon[1].layer not in layers:
                    pgons.append(pgon)
            params.cell.polygons = pgons
    return None


def Layer_Difference(Remove_layer, From_layer, cell_name):
    pgons = merge_polygons(cell=cell_name, layers=[Remove_layer, From_layer])
    remove_polygons(cell=cell_name, layers=[Remove_layer, From_layer])  # optional
    pdiff = nd.clipper.diff_polygons(pgons[From_layer], pgons[Remove_layer])
    for pol in pdiff:
        nd.Polygon(points=pol, layer=From_layer).put(0)
    nd.netlist.pin2pin_drc_off()
    return cell_name









def Crosses(dimension_in, dimension_out, layer_in, layer_out):
    with nd.Cell("Cross") as Cross_AM:
        w=dimension_in
        s=dimension_in
        cross_in = nd.Polygon(layer=layer_out, points=[(-w,-s/2),
                                                 (-w,s/2),
                                                 (-w/2,s/2),
                                                 (-w/2,s),
                                                 (w/2,s),
                                                 (w/2,s/2),
                                                 (w,s/2),
                                                 (w,-s/2),
                                                 (w/2,-s/2),
                                                 (w/2,-s),
                                                 (-w/2,-s),
                                                 (-w/2,-s/2),
                                                 (-w,-s/2)])
        w = dimension_out
        s = dimension_out
        cross_out = nd.Polygon(layer=layer_in, points=[(-w+5,-s/2),
                                                 (-w+5,s/2),
                                                 (-w/2,s/2),
                                                 (-w/2,s-5),
                                                 (w/2,s-5),
                                                 (w/2,s/2),
                                                 (w-5,s/2),
                                                 (w-5,-s/2),
                                                 (w/2,-s/2),
                                                 (w/2,-s+5),
                                                 (-w/2,-s+5),
                                                 (-w/2,-s/2),
                                                 (-w,-s/2)])
        cross_out.put(0,0)
        cross_in.put(0,0)
    return Cross_AM


with nd.Cell("Crosses AMs") as crosses_ams:
    distance_corsses = 400
    for i in range((5000-500)//distance_corsses-2):
        var=10
        Crosses(20+var*i, 30+var*i, i+2, 'EBL AM').put((distance_corsses+2*var)*i,0)
        #Layer_Difference(i+2, 'EBL AM', i+2)
crosses_ams.put(-500-1360+140,-2300)


nd.export_gds(filename='VTEC_Logo.gds')
