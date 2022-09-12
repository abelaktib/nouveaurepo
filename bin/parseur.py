import numpy as np
from Bio.PDB import PDBParser
from objr import obj_atom


def parse(fichier: str):
    '''This function will take the previously inserted .pdb file to create objects
 whose attributes are the elements that will be used to calculate the 
 accessibility of solvent
    Parameters:
        fichier (str): pdb file path

    Returns:
        atom_list(list) : is a list of obj
        o (int) : is a counter of atoms
 '''
    p = PDBParser()
    # opening and reading the pdb file with the biopython module
    s = p.get_structure("", fichier)
    o = 0
    atom_list = []  # list that will contain all the objects created
    for chains in s:  # This loop allows to browse the lines of our .pdb
        for chain in chains:
            for residue in chain:
                # Take only line starting with ATOM on pdb file
                if residue.get_full_id()[3][0] == " ":
                    for atom in residue:
                        atom_list.append(obj_atom(o, int(atom.get_full_id()[3][1]), atom.get_vector()[0], atom.get_vector()[
                            1], atom.get_vector()[2], atom.get_name()[0:1], str(atom.get_parent())[9:12]))

                        o += 1  # o is a counter of atoms
    return atom_list, o
