# DGGSForPoly

This repo contains a 2 packages. 

## poly_fill
Contains a module with a function that, given an inputted Polygon (or set of Polygons) and a desired resolution, the returns a (optionally hybridized) set of rHEALPIX DGGS cells that describe the geometry of the inputted polygon. 

The function is built on top of the AusPIX DGGS Engine (https://github.com/GeoscienceAustralia/AusPIX_DGGS/) and makes use of Shapely's Binary Predicates (which is a ppossible area for future optimisation).

### Fill Strategies
The function has 3 fill_strategies:   
    1) poly_fully_covered_by_cells -  returns a set of cells that completly encapsulating the polygon -> over estimates area   
    2) cells_fully_contained_in_poly -  returns a set of cells whose centroids are contained by the polygon.   
    3) cells_fully_contained_in_poly -  returns a set of cells completely *encapsulated by* the Polygon -> under estimates area   

## cell_operations
Contains modules for calculating area of cell list and for visualising sets of cells and the polygon theyb represent. poly_fill utilises some functions in the helper module.  

See the usage notebook inside of the dggs_for_poly package for a demonstration. 