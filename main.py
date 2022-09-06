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



coords_array = np.empty([100,3])

for x in range(4) :
    coords = defsphere.sphere(dtf, x)
    coords_array = np.concatenate((coords, coords), axis=None)
print(coords_array)


 #coords_array [x] = coords
#print(coords_array)

