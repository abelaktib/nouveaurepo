from Bio.PDB import PDBParser
import math
from objr import obj_atom



rayon_Vdw_s = {"C": 3.1, "O": 2.8, "N": 2.9, "S": 3.25, "CU": 2.8, "CL": 2.9 , "H": 2.5, "P": 3.2} # radius of individual atoms + van der Walls radius


def sphere(atom_list: list, num_atom : int, samples=92): 
    '''This function will generate a 92 point sphere centred around our
 atom which will have the radius of the atom + the van Der Walls radius
 This function add new attribut att obj_atom
    Parameters:
        atom_list(list) : is a list of obj
        num_atom (int) : id of atom    
     
    Returns:
        atom_list(list) : is a list of obj

 '''
    center = [atom_list[num_atom].get_x(),atom_list[num_atom].get_y(),atom_list[num_atom].get_z()] # Coordinates of the centre of the sphere
    element = atom_list[num_atom].get_elements() # Chemistry element name
    rayon_sphere = rayon_Vdw_s[element] # select the good radius
    atom_list[num_atom].set_rayon_sphere(rayon_sphere) # attribution of radius by element name
    points = []
    phi = math.pi * (3 - math.sqrt(5))  # golden angle 
    atom_list[num_atom].set_center(center)
    for i in range(samples):
        y = 1 - (i / float(samples - 1)) * 2  # y axis
        r = math.sqrt(1 - y*y)  # cercle radius
        theta = phi * i  # golden angle increment

        y = y * rayon_sphere + center[1]
        x = r * math.cos(theta) * rayon_sphere + center[0]

        z = r * math.sin(theta) * rayon_sphere + center[2]

        points.append((x, y, z))
    atom_list[num_atom].set_point_sphere(points)

    return atom_list #return all object 'list' with new attributs

