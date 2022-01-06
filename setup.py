import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="DGGSForPoly",
    version="0.2.8",
    author="Ross Petridis",
    author_email="ross.petridis@csiro.au",
    description="This package finds the rHEALPIX dggs cells for Polygons using the AusPIX dggs engine by Geoscience Australia.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/CSIRO-enviro-informatics/vac-project-2021-dggs",
    project_urls={
        "Bug Tracker": "https://github.com/CSIRO-enviro-informatics/vac-project-2021-dggs/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "dggs_for_poly"},
    packages=setuptools.find_packages(where="dggs_for_poly"),
    python_requires=">=3.9",
    
    install_requires = [
        'matplotlib',
        'shapely',
        'geopandas',
        'autopep8',
        'ipykernel',
        'contextily',
        'requests',
        'geojson',
        'ipyleaflet',
        'scipy',
        'pygeoj',
        'numba',
    ],
    
    
    dependency_links = [
        'git+https://github.com/manaakiwhenua/rhealpixdggs-py.git',
        'git+https://github.com/CSIRO-enviro-informatics/AusPIX_DGGS.git'
    ]
    
    
)