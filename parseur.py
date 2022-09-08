import numpy as np
import pandas as pd
from Bio.PDB import PDBParser
from objr import Chien


def parse(fichier):
    # data = {"residues": [], "x": [], "y": [], "z": [], "element": []}
    p = PDBParser()
    s = p.get_structure("", fichier)
    o = 0
    # num_atom = []
    # residues = []
    # x = []
    # y = []
    # z = []
    # elements = []
    # aa = []
    atom_list = []
    for chains in s:
        for chain in chains:
            for residue in chain:
                for atom in residue:
                    atom_list.append(Chien(o, int(atom.get_full_id()[3][1]), atom.get_vector()[0], atom.get_vector()[
                                    1], atom.get_vector()[2], atom.get_name()[0:1], str(atom.get_parent())[8:12]))
                    # num_atom.append(o)
                    # residues.append(int(atom.get_full_id()[3][1]))
                    # x.append(atom.get_vector()[0])
                    # y.append(atom.get_vector()[1])
                    # z.append(atom.get_vector()[2])
                    # elements.append(atom.get_name()[0:1])
                    # aa.append(str(atom.get_parent())[8:12])
                    o += 1

    # data["num_atom"] = num_atom
    # data["residues"] = residues
    # data["x"] = x
    # data["y"] = y
    # data["z"] = z
    # data["element"] = elements
    # data["aa"] = aa


    # data_df = pd.DataFrame(data)

    return atom_list, o


parse("1bja.pdb")
