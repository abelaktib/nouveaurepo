import numpy as np
import pandas as pd
from Bio.PDB import PDBParser
import math
import matplotlib.pyplot as pp
from objr import Chien


rayon_Vdw_s = {"C": 3.1, "O": 2.8, "N": 2.9, "S": 3.25, "CU": 2.8, "CL": 2.9 , "H": 2.5, "P": 3.2}


def sphere(atom_list, num_atom, samples=92):
    center = [atom_list[num_atom].get_x(),atom_list[num_atom].get_y(),atom_list[num_atom].get_z()]
    element = atom_list[num_atom].get_elements()
    rayon_sphere = rayon_Vdw_s[element]
    atom_list[num_atom].set_rayon_sphere(rayon_sphere)
    points = []
    phi = math.pi * (3 - math.sqrt(5))  # golden angle
    atom_list[num_atom].set_center(center)
    for i in range(samples):
        y = 1 - (i / float(samples - 1)) * 2  # y axis
        r = np.sqrt(1 - y*y)  # cercle radius
        theta = phi * i  # golden angle increment

        y = y * rayon_sphere + center[1]
        x = r * np.cos(theta) * rayon_sphere + center[0]

        z = r * np.sin(theta) * rayon_sphere + center[2]

        points.append((x, y, z))
    atom_list[num_atom].set_point_sphere(points)



    return atom_list


    # # _array # points_coordinates, #pp.show()
        #i = np.arange(samples)


    # center = data_df.loc[num_atome, ["x", "y", "z"]]
    # element = data_df.loc[num_atome, "element"]
    # residues = data_df.loc[num_atome, "residues"]
    #     
    # center = (center[0], center[1], center[2])
    # points.append(center)
    # rayon_sphere = (rayon_sphere, rayon_sphere)
    # points.append((rayon_sphere))
    # points.append((residues))
    # #points_array = np.array(points)