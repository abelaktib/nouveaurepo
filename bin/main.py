from objr import obj_atom
import parseur
import defsphere
import math
import asa



def display_asa(asa_abs: dict, asa_rel: dict):
    for key in asa_abs:
        print(
            f"id residue:{str(key).ljust(13,' ')} - asa_abs (Å**2):{str(asa_abs[key]).ljust(20,' ')} - asa_rel (Å**2):{asa_rel[key]}")


def main():
    
    print(''' This program uses 3 different functions to: parse our pdb files,
create spheres centred on our atoms of interest and calculate the
      solvent accessibility''')


    files = str(input("Enter your .pdb file path:"))

    # Parsing of the chosen pdb file to retrieve all atoms as objects with o the total number of atoms
    atom_list, o = parseur.parse(files)

    for a in range(o):  # For each atom in all atoms in pdb
        # Creation of fibonacci spheres for each atom
        atom_list = defsphere.sphere(atom_list, a)

    point_total = 92 * o  # counting the number of points in all spheres

    asa_abs, asa_rel, porcent_accessibilite, asa_abs_sum = asa.asa(
        atom_list)  # collection of accessibility results

    # print(f"La surface accessible au solvant par résidu est de (A**2) : {asa_abs} " )

    # print(f"La surface accessible relatif au solvant par résidu est de (A**2): {asa_rel} " )
    print("Les surfaces absolues et relatives accessibles aux solvants par résidu sont les suivantes :")
    display_asa(asa_abs, asa_rel)
    print("")

    print(f"Le poucentage d'accessibilité est de: {porcent_accessibilite} ")

    print(f"La surface accessible au solvant est de {asa_abs_sum}Å**2")


if __name__ == "__main__":
    main()

