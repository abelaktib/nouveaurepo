from turtle import distance
import parseur
import defsphere
import math
#import plotly.express as px
import numpy as np
import pandas as pd


atom_list, o = parseur.parse("1bja.pdb")


for a in range(o):
    atom_list = defsphere.sphere(atom_list, a)

    # coords_a.append(coords)

# surface_noncontact = 0
# surface_total = 0

point_total_list = []
point_noncontact_list = []


for atom_un in atom_list:
    point_noncontact = 0
    point_total = 0
    for atom_deux in atom_list:
        if atom_un != atom_deux:
            atom_un_centre = atom_un.get_center()
            atom_deux_centre = atom_deux.get_center()
            distance_centre = math.dist(atom_un_centre, atom_deux_centre)
            if distance_centre < 10:
                for point_sphere in atom_un.get_point_sphere():
                    distance_sphere_centre = math.dist(point_sphere, atom_deux_centre)
                    rayon_atom_deux_ss = float(atom_deux.get_rayon_sphere())
                    if distance_sphere_centre < rayon_atom_deux_ss:
                        point_noncontact += 1
                        point_total += 1
                    else:
                        point_total += 1

    atom_un.set_point_total(point_total)
    atom_un.set_point_noncontact(point_noncontact)
    # print(atom_un.get_point_total(),)
    # print(atom_un.get_point_noncontact())


surface_residu_noncontact = {}
surface_residu_total = {}

for atom_un in atom_list:
  atom_un.set_surface_total()
  atom_un.set_surface_noncontact()
  # print(atom_un.get_surface_total())

  if (atom_un.get_residues(), atom_un.get_aa()) in surface_residu_noncontact:
    surface_residu_noncontact[(atom_un.get_residues(), atom_un.get_aa())] += atom_un.get_surface_noncontact()
  else:
      surface_residu_noncontact[(atom_un.get_residues(), atom_un.get_aa())] = atom_un.get_surface_noncontact()

#   if (atom_un.get_residues(), atom_un.get_aa()) in surface_residu_total:
#     surface_residu_total[(atom_un.get_residues(),atom_un.get_aa())] += atom_un.get_surface_total()
#   else:
#       surface_residu_total[(atom_un.get_residues(), atom_un.get_aa())] = atom_un.get_surface_total()

print(sum(surface_residu_noncontact.values()))    #ASA abs

# point_contact = point_total - point_noncontact

# print(point_contact)
