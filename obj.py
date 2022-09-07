class Chien:
    def __init__(self, num_atom=None, residues=None, x=None, y=None, z=None, elements= None, aa=None):
        self.set_num_atom(num_atom)
        self.set_residues(residues)
        self.set_x(x)
        self.set_y(y)
        self.set_y(z)
        self.set_elements(elements)
        self.set_aa(aa)

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
