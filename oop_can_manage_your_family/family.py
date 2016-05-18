from datetime import date
class Person():
    EYES_COLORS = ["Blue", "Green", "Brown"]
    GENRES = ["Female", "Male"]
    ''' Public Method '''
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
        # Checks for the lenght of the list date_of_birth and its values to see if they are ints
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

    #Returns a string that has the name and last name of the person concatenated
    def __str__(self):
         return "%s %s" %(self.__first_name , self.last_name)

    def is_male(self):
        if self.__genre is "Male":
            return True
        else:
            return False

    def age(self):
        today = date.today()
        age = today.year - self.__date_of_birth[2] - ( (today.month, today.day) < (self.__date_of_birth[1], self.__date_of_birth[0]))
        return age
    def __gt__(self,other):
        return (self.age() > other.age())
