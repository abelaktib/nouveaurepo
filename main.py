from turtle import distance
import parseur
import defsphere
import math
#import plotly.express as px
import numpy as np
import pandas as pd


dtf, o = parseur.parse("1bja.pdb")
print(dtf)


coords_a = []
for a in range(o):
    coords = defsphere.sphere(dtf, a)
    coords_a.append(coords)

# print(coords_a[1][101][1])
# print(coords_a[1][100][101]) #coords_a[sphere] il existe 1 sphere par atome
    # coords_a[sphere] [point d une sphere] il en existe 100 le 100eme est le centre de la sphere le 101 est le rayon
    # coords_a[sphere] [point d une sphere] [1,2,2] coordonnées d un points x y z
    # coords_a[sphere][101][1] rayon de la sphere924

surface_noncontact = 0
surface_total = 0

point_total_list = []
point_noncontact_list = []


for atom_un in coords_a:
    point_noncontact = 0
    point_total = 0

    for atom_deux in coords_a:
        if atom_un != atom_deux:
            atom_un_centre = atom_un[92]
            atom_deux_centre = atom_deux[92]
            distance_centre = math.dist(atom_un_centre, atom_deux_centre)
            if distance_centre < 10:
                for point_sphere in atom_un[0:92]:
                    distance_sphere_centre = math.dist(
                        point_sphere, atom_deux_centre)
                    # rayon_atom_un_ss = rayon atom 1 sans sonde
                    rayon_atom_un_ss = float(atom_un[93][1] - 1.4)
                    if distance_sphere_centre > rayon_atom_un_ss:
                        point_noncontact += 1
                        point_total += 1
                    else:
                        point_total += 1
    point_total_list.append(point_total)
    point_noncontact_list.append(point_noncontact)

print(point_total_list)
print(point_noncontact_list)




# point_contact = point_total - point_noncontact

# print(point_contact)
