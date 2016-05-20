from sys import argv
from datetime import date
import json
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
        self.is_married_to = 0

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
    def __eq__(self, other):
        return(self.age() == other.age())
    def __ne__(self, other):
        return (self.age() != other.age())
    def __ge__(self, other):
        return (self.age >= other.age())
    def __lt__(self, other):
        return (self.age < other.age())
    def __le__(self, other):
        return (self.age <= other.age())

    ''' Creating a diccionary '''
    def json(self):
        dicc ={
        'id':self.__id,
        'eyes_color':self.__eyes_color,
        'genre':self.__genre,
        'date_of_birth':self.__date_of_birth,
        'first_name':self.__first_name,
        'last_name':self.last_name,
        'is_married_to':self.is_married_to
        }
        return dicc

    ''' loading json'''
    def load_from_json(self, json):
    #    if json is not dict:
    #        raise Exception("json is not valid")
        self.__id = json['id']
        self.__eyes_color = json['eyes_color']
        self.__genre = json['genre']
        self.__date_of_birth = json['date_of_birth']
        self.__first_name = json['first_name']
        self.last_name = json['last_name']
        self.is_married_to = json['is_married_to']


class Baby(Person):
    ''' '''
    def __init__(self, id, first_name, date_of_birth, genre, eyes_color):
        Person.__init__(self, id, first_name, date_of_birth, genre, eyes_color)
    def can_run(self):
        return False
    def need_help(self):
        return True
    def is_young(self):
        return True
    def can_vote(self):
        return False
    '''Begining of the marriage methods'''
    def can_be_married(self):
        return False
    def is_married(self):
        if self.is_married_to is not 0:
            return True
        else:
            return False
    def divorce(self, p):
        return False
    def just_married_with(self, p):
        return False
class Teenager(Person):
    ''' '''
    def __init__(self, id, first_name, date_of_birth, genre, eyes_color):
        Person.__init__(self, id, first_name, date_of_birth, genre, eyes_color)
    def can_run(self):
        return True
    def need_help(self):
        return False
    def is_young(self):
        return True
    def can_vote(self):
        return False
    '''Begining of the marriage methods'''
    #returns true if is adult or senior
    def can_be_married(self):
        return False
    #returns false if is_married_to = 0
    def is_married(self, p):
        if self.is_married_to is not 0:
            return True
        else:
            return False
    def divorce(self, p):
        return False
    def just_married_with(self, p):
        return False
class Adult(Person):
    def __init__(self, id, first_name, date_of_birth, genre, eyes_color):
        Person.__init__(self, id, first_name, date_of_birth, genre, eyes_color)
    def can_run(self):
        return True
    def need_help(self):
        return False
    def is_young(self):
        return False
    def can_vote(self):
        return True
    '''Begining of the marriage methods'''
    #returns true if is adult or senior
    def can_be_married(self):
        return True
    #returns false if is_married_to = 0
    def is_married(self):
        if self.is_married_to is not 0:
            return True
        else:
            return False
    #will unlink 2 persons => assign is_married_to of each person to 0. Don't change the last_name, it's too late!
    def divorce(self, p):
        ''''''
        self.is_married_to = 0
        p.is_married_to = 0

    def just_married_with(self, p):
        ''''''
        self.is_married_to = p.__id
class Senior(Person):
    def __init__(self, id, first_name, date_of_birth, genre, eyes_color):
        Person.__init__(self, id, first_name, date_of_birth, genre, eyes_color)
    def can_run(self):
        return False
    def need_help(self):
        return True
    def is_young(self):
        return False
    def can_vote(self):
        return True
    def can_be_married(self):
        return True
    '''Begining of the marriage methods'''
    def is_married(self):
        if self.is_married_to is not 0:
            return True
        else:
            return False
    def divorce(self, p):
        ''''''
        self.is_married_to = 0
        p.is_married_to = 0
    def just_married_with(self, p):
        ''''''
        self.is_married_to = p.__id

def save_to_file(list, filename):
    with open(filename, 'w') as outfile:
        list_of_json_strings = []
        for i in list:
            list_of_json_strings.append(i.json())
        outfile.write(json.dumps(list_of_json_strings,indent = 2))

def load_from_file(filename):
    data = []
    p = Person(1, "Julien", [12, 24, 1980], "Male", "Blue")
    with open(filename, 'r') as data_file:
        a = json.load(data_file)
        for line in a:
            p.load_from_json(line)
            data.append(p)
        return data
