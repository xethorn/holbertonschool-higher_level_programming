class Person():
    EYES_COLORS = ["Blue", "Green", "Brown"]
    GENRES = ["Female", "Male"]
    def __init__(self, id, first_name, date_of_birth, genre, eyes_color):
        ''' Private '''
        if id < 0 and isinstance(id, int):
            raise Exception("id is not an integer")
        self.__id = id

        if eyes_color not in Person.EYES_COLORS:
            raise Exception("eyes_color is not valid")
        self.__eyes_color = eyes_color

        if genre not in Person.GENRES:
            raise Exception("genre is not valid")
        self.__genre = genre

        if len(date_of_birth) is 3 and all(isinstance (n, int) for n in date_of_birth):
            self.__date_of_birth = date_of_birth
        else:
            raise Exception("date_of_birth is not a valid date")

        if first_name is " " and isinstance(first_name, str):
            raise Exception("string is not a string")
        self.__first_name = first_name

        ''' Public '''
        self.last_name = " "

    ''' Getters '''
    def get_id(self):
        return self.__id

    def get_eyes_color(self):
        return self.__eyes_color

    def get_genre(self):
        return self.__genre

    def get_date_of_birth(self):
        return self.__date_of_birth

    def get_first_name(self):
        return self.__first_name
