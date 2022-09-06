import numpy as np
import pandas as pd
from Bio.PDB import PDBParser
import math
import matplotlib.pyplot as pp

rayon_Vdw_s = {"C": 2.3, "O": 2.12, "N": 2.15, "S": 2.4, "CU": 2.0, "CL": 2.1}

def sphere(data_df, num_atome, samples=100):
    center = data_df.loc[num_atome, ["x", "y", "z"]]
    element = data_df.loc[num_atome, "element"]
    rayon_sphere = rayon_Vdw_s[element]
    points = []
    phi = math.pi * (3 - math.sqrt(5))  # golden angle
    for i in range(samples):
        #i = np.arange(samples)
        y = 1 - (i / float(samples - 1)) * 2  # z axis
        r = np.sqrt(1 - y*y)  # cercle radius
        theta = phi * i  # golden angle increment

        y = y * rayon_sphere + center[1]
        x = r * np.cos(theta) * rayon_sphere + center[0]
        
        z = r * np.sin(theta) * rayon_sphere + center[2]

        points.append((x,y,z))
        #points_array = np.array(points)
    
    # points[:, 0] = x
    # points[:, 1] = y
    # points[:, 2] = z

    #points_coordinates = pd.DataFrame(columns=["x", "y", "z"], data=points)
    # pp.figure().add_subplot(projection="3d").scatter(x, y, z)

    return points #_array # points_coordinates, #pp.show()