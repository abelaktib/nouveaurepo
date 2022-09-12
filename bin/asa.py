import math
from objr import obj_atom
import parseur
import defsphere

def asa(atom_list: list):
    '''This function uses obj_atom objects to calculate the solvent
     accessibility of a protein whose objects are obtained
    Parameters:
        atom_list(list) : is a list of obj

    Returns:
        asa_abs (list) : solvent accessibility by residues
        asa_rel (list) : relative solvent accessibility  by residues
        porcent_accessibilite (float) : porcent of accessibility
        asa_abs_sum (float) : solvent accessibility of protein

 '''
    for atom_un in atom_list:     # For each atom, select these neighbours
        atom_un.set_list_nc()
        for atom_deux in atom_list:
            if atom_un != atom_deux:
                atom_un_centre = atom_un.get_center()
                atom_deux_centre = atom_deux.get_center()
                distance_centre = math.dist(atom_un_centre, atom_deux_centre)
                if distance_centre < 10: #I f the distance between these neighbours is less than 10 Angstrom
                    for i in range(len(atom_un.get_point_sphere())):
                        point_sphere = atom_un.get_point_sphere()[i]
                        distance_sphere_centre = math.dist(
                            point_sphere, atom_deux_centre)
                        rayon_atom_deux = float(atom_deux.get_rayon_sphere()) # Compare the distance from a point on the sphere to the centre of the second sphere to the size of the radius
                        if distance_sphere_centre < rayon_atom_deux: #
                            atom_un.get_list_nc()[i] = 1 #Compare the distance from a point on the sphere to the centre of the second sphere to the size of the radius

            enfoui = (atom_un.get_list_nc()) # Number of points buried
        atom_un.set_point_total(92) # total number of point
        atom_un.set_point_noncontact(92-sum(enfoui)) #Number of points exposed

# Calcul of ASA by residue
    surface_residu_noncontact = {} 
    surface_residu_total = {}


    for atom_un in atom_list:
        atom_un.set_surface_atome()
        atom_un.set_surface_noncontact()

        if (atom_un.get_residues(), atom_un.get_aa()) in surface_residu_noncontact:
            surface_residu_noncontact[(atom_un.get_residues(
            ), atom_un.get_aa())] += atom_un.get_surface_noncontact()
        else:
            surface_residu_noncontact[(atom_un.get_residues(
            ), atom_un.get_aa())] = atom_un.get_surface_noncontact()

        if (atom_un.get_residues(), atom_un.get_aa()) in surface_residu_total:
            surface_residu_total[(atom_un.get_residues(),atom_un.get_aa())] += atom_un.get_surface_atome()
        else:
            surface_residu_total[(atom_un.get_residues(), atom_un.get_aa())] = atom_un.get_surface_atome()


# Results of ASA by residues and sum 
    asa_abs = surface_residu_noncontact
    asa_total = surface_residu_total

    asa_total_sum = sum(surface_residu_total.values())

    asa_abs_sum = sum(surface_residu_noncontact.values())

    porcent_accessibilite = (asa_abs_sum / asa_total_sum) *100


    asa_max = {  # Max ASA :  https://en.wikipedia.org/wiki/Relative_accessible_surface_area
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
# Calcul of relative ASA
    asa_rel = {}

    for key in asa_abs.keys() :
        if key[1] in asa_max.keys():
            asa_rel[key] = asa_abs[key] / asa_max[key[1]]


    asa_rel_sum = sum(asa_rel.values())

    return asa_abs,asa_rel,porcent_accessibilite,asa_abs_sum
