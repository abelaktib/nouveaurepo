from objr import Chien
import parseur
import defsphere
import math
#import plotly.express as px
import numpy as np
import pandas as pd


atom_list, o = parseur.parse("2ml6.pdb")


for a in range(o):
    atom_list = defsphere.sphere(atom_list, a)

    # coords_a.append(coords)

# surface_noncontact = 0
# surface_total = 0

point_total = 92 * o


for atom_un in atom_list:
    atom_un.set_list_nc()
    for atom_deux in atom_list:
        if atom_un != atom_deux:
            atom_un_centre = atom_un.get_center()
            atom_deux_centre = atom_deux.get_center()
            distance_centre = math.dist(atom_un_centre, atom_deux_centre)
            if distance_centre < 10:
                for i in range(len(atom_un.get_point_sphere())):
                    point_sphere = atom_un.get_point_sphere()[i]
                    distance_sphere_centre = math.dist(
                        point_sphere, atom_deux_centre)
                    rayon_atom_deux = float(atom_deux.get_rayon_sphere())
                    if distance_sphere_centre < rayon_atom_deux:
                        atom_un.get_list_nc()[i] = 1

        enfoui = (atom_un.get_list_nc())
    atom_un.set_point_total(92)
    atom_un.set_point_noncontact(92-sum(enfoui))

    # print(atom_un.get_point_noncontact())
    # print(atom_deux.get_point_noncontact())


surface_residu_noncontact = {}
surface_residu_total = {}


for atom_un in atom_list:
    atom_un.set_surface_atome()
    atom_un.set_surface_noncontact()
    # print(atom_un.get_point_total())
    # print(atom_un.get_surface_atome())
#   print(atom_un.get_surface_noncontact())

    if (atom_un.get_residues(), atom_un.get_aa()) in surface_residu_noncontact:
        surface_residu_noncontact[(atom_un.get_residues(
        ), atom_un.get_aa())] += atom_un.get_surface_noncontact()
    else:
        surface_residu_noncontact[(atom_un.get_residues(
        ), atom_un.get_aa())] = atom_un.get_surface_noncontact()

#   if (atom_un.get_residues(), atom_un.get_aa()) in surface_residu_total:
#     surface_residu_total[(atom_un.get_residues(),atom_un.get_aa())] += atom_un.get_surface_atome()
#   else:
#       surface_residu_total[(atom_un.get_residues(), atom_un.get_aa())] = atom_un.get_surface_atome()

# print(surface_residu_noncontact)  # ASA abs
asa_abs = surface_residu_noncontact
asa_abs_sum = sum(surface_residu_noncontact.values())
# # point_contact = point_total - point_noncontact

# # print(point_contact)


asa_max = {
    'CYS': 167.0,
    'ASP': 193,
    'SER': 155,
    'GLN': 225,
    'LYS': 236,
    'ILE': 197,
    'PRO': 159,
    'THR': 172,
    'PHE': 240,
    'ASN': 195,
    'GLY': 104,
    'HIS': 224,
    'LEU': 201,
    'ARG': 274,
    'TRP': 285,
    'ALA': 129,
    'VAL': 174,
    'GLU': 223,
    'TYR': 263,
    'MET': 224
}

asa_rel = {}

for key in asa_abs.keys() :
    # print(key[1])
    asa_rel[key] = asa_abs[key] / asa_max[key[1][1:]]
print(asa_rel)

asa_rel_sum = sum(asa_rel.values())
print(asa_rel_sum )

#asa_abs[(1, "GLYS")] / asa_max[(1, "GLYS")[1]]
