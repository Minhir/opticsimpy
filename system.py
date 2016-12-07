from numpy import identity, dot
from light import Light


class System:

    def __init__(self):
        self.matrix = identity(4)
        self.elements_list = [self.matrix]

    def _calculate_(self, element):
        self.matrix = dot(element.get_matrix(), self.matrix)

    def add_elements(self, *elements):
        for element in elements:
            self.elements_list.append(element.get_matrix())
            self._calculate_(element)

    def count(self, ray):
        el = dot(self.matrix, ray.get_matrix())
        return Light(float(el[0]), float(el[1]), float(el[2]), float(el[3]))

    def get_elements_list(self):
        return self.elements_list

    def get_matrix(self):
        return self.matrix
