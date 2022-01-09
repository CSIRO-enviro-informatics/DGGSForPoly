from DGGSForPoly import poly_fill
from get_data import get_static_test_data_Black_Mountain, get_poly_fill_ex2_answer
from DGGSForPoly.cell_area import area_of_cells
from math import isclose

# Testing from entire geojson 
def test_poly_fill_from_geojson_ex1():
    geojson_obj = get_static_test_data_Black_Mountain()
    list_of_lists_of_dggs_cells = poly_fill.poly_fill_from_geojson(geojson_obj=geojson_obj, max_res=10, fill_strategy='poly_fully_covered_by_cells')

    cells_answers = get_poly_fill_ex2_answer()
    area_answers = [28484442.697446138, 805472.6726784256, 8249992.829251752]
    
    for i,cell_list in enumerate(list_of_lists_of_dggs_cells):
        cell_list.sort()
        assert cell_list ==  cells_answers[i]
        area = area_of_cells(cells=cell_list)
        assert(isclose(area, area_answers[i] , abs_tol = 0.00001 ))


