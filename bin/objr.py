import math

class obj_atom:
    '''The class obj_atom takes all the elements obtained from the .pdb 
file as well as new attributes allowing the calculation of the 
accessibility of the solvent
...
Attributes
    ----------
    num_atom : int
        id atom     
    residues : int
        id residu
    x : float
        x position of atom
    y : float
        y position of atom
    z : float
        z position of atom
    elements : str 
        chemstry element name
    aa : str
        residue name 
    rayon_sphere : float
        radius of the sphere
    point_sphere : list of tuple
        (x,y,z) of each point of the sphere
    center : tuple
        (x,y,z) of the center of the sphere
    point_noncontact : int
        number of point exposed
    point_total : int
        total point on sphere
    surface_atome: float
        surface of sphere of the atom 
    surface_noncontact : float
    surface of the sphere accessible to solvant
    list_nc : list of boolean
        flag for each point of sphere accessible or not
'''
    def __init__(self, num_atom=None, residues=None, x=None, y=None, z=None, elements=None, aa=None, rayon_sphere=None, point_sphere=None, center=None,point_total = None, point_noncontact = None, surface_atome= None, surface_noncontact=None,list_nc=None):
        self.__num_atom = num_atom # id atom
        self.__residues = residues # id residu
        self.__x = x # x position of atom
        self.__y = y # y position of atom
        self.__z = z  # z position of atom
        self.__elements = elements # the chemstry element name
        self.__aa = aa # residue name 
        self.__rayon_sphere = rayon_sphere # radius of the sphere
        self.__point_sphere = point_sphere # x,y,z of each point of the sphere
        self.__center = center # x,y,z of the center of the sphere
        self.__point_noncontact =  point_noncontact # number of point exposed
        self.__point_total = point_total # how much point of the sphere is accessible to the solvent
        self.__surface_atome = surface_atome # surface of sphere of the atom 
        self.__surface_noncontact = surface_noncontact # surface of the sphere accessible to solvant
        self.__list_nc = list_nc # flag for each point of sphere accessible or not

    def get_num_atom(self):
        return self.__num_atom

    def set_num_atom(self, num_atom):
        self.__num_atom = num_atom

    def get_residues(self):
        return self.__residues

    def set_residues(self, residues):
        self.__residues = residues

    def get_x(self):
        return self.__x

    def set_x(self, x):
        self.__x = x

    def get_y(self):
        return self.__y

    def set_y(self, y):
        self.__y = y

    def get_z(self):
        return self.__z

    def set_z(self, z):
        self.__z = z

    def get_elements(self):
        return self.__elements

    def set_elements(self, elements):
        self.__elements = elements

    def get_aa(self):
        return self.__aa

    def set_aa(self, aa):
        self.__aa = aa

    def get_rayon_sphere(self):
        return self.__rayon_sphere

    def set_rayon_sphere(self, rayon_sphere):
        self.__rayon_sphere = rayon_sphere

    def get_point_sphere(self):
        return self.__point_sphere

    def set_point_sphere(self, point_sphere):
        self.__point_sphere = point_sphere

    def get_center(self):
        return self.__center

    def set_center(self, center):
        self.__center = center

    def get_point_noncontact(self):
        return self.__point_noncontact

    def set_point_noncontact(self, point_noncontact):
        self.__point_noncontact = point_noncontact

    def get_list_nc(self):
        return self.__list_nc

    def set_list_nc(self):
        self.__list_nc = [0]*92

    def get_point_total(self):
        return self.__point_total

    def set_point_total(self, point_total):
        self.__point_total = point_total

    def get_surface_atome(self):
        return self.__surface_atome

    def set_surface_atome(self):
        self.__surface_atome = (4 * math.pi * (self.__rayon_sphere)**2)

    def get_surface_noncontact(self):
        return self.__surface_noncontact

    def set_surface_noncontact(self):
        self.__surface_noncontact = (self.__surface_atome * self.__point_noncontact)/self.__point_total

    def __str__(self):
        return "[ " + str(self.__num_atom) + "]" #print an object will print his num_atom+
