import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="DGGSForPoly",
    version="0.2.16",
    author="Ross Petridis",
    author_email="ross.petridis@csiro.au",
    description="This package finds the rHEALPIX dggs cells for Polygons using the AusPIX dggs engine by Geoscience Australia.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/CSIRO-enviro-informatics/vac-project-2021-dggs",
    project_urls={
        "Bug Tracker": "https://github.com/CSIRO-enviro-informatics/vac-project-2021-dggs/issues",
    },
    #package_dir={"": "."}, # This directory
    #packages=setuptools.find_packages(where="."), # This directory
    
    #packages = ['cell_operations', 'poly_fill'], 
    packages=setuptools.find_packages(),


    install_requires = [
        'Shapely',
        'geopandas',
        'geojson',
        'ipyleaflet',
        'pandas',
    ],
    
    dependency_links = [
        'git+https://github.com/manaakiwhenua/rhealpixdggs-py.git',
        'git+https://github.com/CSIRO-enviro-informatics/AusPIX_DGGS.git'
    ]
    
    
)