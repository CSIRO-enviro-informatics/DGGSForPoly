from DGGSForPoly import poly_fill

def poly_fill_ex1():
    geojson_data = get_static_test_data()
    geojson_geom = geojson_data['features'][0]['geometry']
    cells = poly_fill.poly_fill(geojson=geojson_geom, max_res=8)
    cells.sort()
    print(cells)

def get_static_test_data():
    return {
         "type": "FeatureCollection",
          "features": [
            {
              "type": "Feature",
              "properties": {},
              "geometry": {
                "type": "Polygon",
                "coordinates": [
                  [
                      [
                      144.8828887939453,
                      -37.91711773774181
                    ],
                    [
                      145.15274047851562,
                      -37.91711773774181
                    ],
                    [
                      145.15274047851562,
                      -37.725650988654515
                    ],
                    [
                      144.8828887939453,
                      -37.725650988654515
                    ],
                    [
                      144.8828887939453,
                      -37.91711773774181
                    ]
                  ]
                ]
              }
            }
          ]
        }



if __name__ == "__main__":
    poly_fill_ex1()

