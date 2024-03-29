import math
'''Class'''
class Circle():

    ''' Constructor '''
    def __init__(self,radius):
        # private attributes
        self.__radius = radius
        self.__center = [0,0]
        self.__color = " "
        # public attributes
        self.name = " "

    ''' Destructor '''
    def __del__(self):
        pass

    ''' Getter '''
    def get_color(self):
        return self.__color

    ''' Setter '''
    def set_color(self, color):
        self.__color = color

    ''' Getter '''
    def get_center(self):
        return self.__center

    ''' Setter '''
    def set_center(self, center):
        self._center = center

    ''' Public Method '''
    def area(self):
        x = self.__radius**2 * math.pi
        return x
