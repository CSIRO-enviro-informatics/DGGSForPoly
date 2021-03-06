# DGGSForPoly

## poly_fill
A function that returns a set of rHEALPIX DGGS cells that describe the geometry of the inputted polygon. 

The function is built on top of the rHealPIX DGGS Engine (https://github.com/manaakiwhenua/rhealpixdggs-py) and makes use of Shapely's Binary Predicates.

See the usage notebook for examples.

#### Fill Strategies
poly_fill() function has 3 fill_strategies:   
    1) poly_fully_covered_by_cells -  returns a set of cells that completly encapsulating the polygon -> over estimates area   
    2) centroids_in_poly -  returns a set of cells whose centroids are contained by the polygon.   
    3) cells_fully_contained_in_poly -  returns a set of cells completely encapsulated *by* the Polygon -> under estimates area   

#### Hierarchical Representation
poly_fill() can return a uniform cell level representation or a hieerarchical representation by changing the value of the 'hybrid' bool. Default is True.

## cell_operations
Contains modules for calculating area of cell list and for visualising sets of cells and the polygon they represent. poly_fill utilises some functions.  

## Setting up environment

```
$ python3 -m venv .venv
$ source .venv/bin/activate
# or on Windows: source .venv/Scripts/activate
$ python setup.py install
```

Include testing
```
$ pip install -U pytest
$ pytest
```
