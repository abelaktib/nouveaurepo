import parseur
import defsphere
import math
import plotly.express as px
import numpy as np
import pandas as pd

#data_df = parseur.parse("1bjj.pdb")

#print(data_df,)

dtf, o = parseur.parse("1bjj.pdb")
print(o)



coords_array = np.empty(1)

for x in range(1) :
    coords = defsphere.sphere(dtf, x)
    coords_arrays = np.stack((coords_array, coords), axis=-1)
    print(coords) #_array)



