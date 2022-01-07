from DGGSForPoly import poly_fill

def func(x):
    return x + 1


def test_answer():
    assert func(3) == 4

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


def test_poly_fill_ex1():
    geojson_data = get_static_test_data()['features'][0]['geometry']
    cells = poly_fill.poly_fill(geojson=geojson_data, max_res=8)
    cells.sort()
    assert cells == ['R78474647', 'R78474648', 'R78474656', 'R78474657', 'R78474658', 'R78474671', 'R78474672', 'R78474674', 'R78474675', 'R78474677', 'R78474678', 'R7847468', 'R78474736', 'R78474737', 'R78474738', 'R78474746', 'R78474747', 'R78474748', 'R78474756', 'R78474757', 'R78474758', 'R7847476', 'R7847477', 'R7847478', 'R78474836', 'R78474837', 'R78474838', 'R78474846', 'R78474847', 'R78474848', 'R78474856', 'R7847486', 'R7847487', 'R78474880', 'R78474883', 'R78474886', 'R78477011', 'R78477012', 'R78477014', 'R78477015', 'R78477017', 'R78477018', 'R7847702', 'R78477041', 'R78477042', 'R78477044', 'R78477045', 'R78477047', 'R78477048', 'R7847705', 'R78477071', 'R78477072', 'R78477074', 'R78477075', 'R78477077', 'R78477078', 'R7847708', 'R784771', 'R7847720', 'R7847721', 'R78477220', 'R78477223', 'R78477226', 'R7847723', 'R7847724', 'R78477250', 'R78477253', 'R78477256', 'R7847726', 'R7847727', 'R78477280', 'R78477283', 'R78477286', 'R78477311', 'R78477312', 'R78477320', 'R78477321', 'R78477322', 'R78477400', 'R78477401', 'R78477402', 'R78477410', 'R78477411', 'R78477412', 'R78477420', 'R78477421', 'R78477422', 'R78477500', 'R78477501', 'R78477502', 'R78477510', 'R78477511', 'R78477512', 'R78477520']

