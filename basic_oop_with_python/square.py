class Square(object):
    '''Constructor'''
    def __init__(self, side_length):
        # private attributes
        self.__side_length = side_length
        self.__center = [0,0]
        self.__color = " "
        # public attributes
        self.name = " "

    def __del__(self):
        pass

    ''' Getter '''
    def get_color(self):
        return self.__color

    ''' Setter '''
    def set_color(self,color):
        self.__color = color

    ''' Getter '''
    def get_center(self):
        return self.__center

    ''' Setter '''
    def set_center(self, center):
        self.__center = center

    def area(self):
        x = self.__side_length**2
        return x

def a():
    for i in range(0,4):
        if i == 0:
            for j in range(0,self.__side_length):
                return "*",
