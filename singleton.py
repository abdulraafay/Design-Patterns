from abc import ABCMeta, abstractstaticmethod
from os import stat

class IPerson(metaclass=ABCMeta):
    
    @abstractstaticmethod
    def print_data():

        ''' Implementation in child class '''

class PersonSingleton(IPerson):
    
    ''' Singleton class responsible for generating one and only one instance '''

    __instance = None

    @staticmethod
    def get_instance():
        # Returns single instance of the class if exists, otherwise creates one and returns
        if PersonSingleton.__instance is None:
            PersonSingleton("Default Name", 0)
        return PersonSingleton.__instance

    def __init__(self, name, age):

        # Instantiate if no instance exist, or raise an exception
        if PersonSingleton.__instance is None:
            self.name = name
            self.age = age
            PersonSingleton.__instance = self

        else:
            raise Exception("Singleton cannot be instantiated more than once.")

    @staticmethod
    def print_data():
        # Print instance data
        print(f'Name is {PersonSingleton.__instance.name} and age is {PersonSingleton.__instance.age}')

# First instantiation
p = PersonSingleton("Syed", 34)
# print(p)
p.print_data()

print(p.get_instance())

# Secpond attempt to instantiate
p1 = PersonSingleton("Mike", 30)
# print(p1)
p1.print_data()

print(p1.get_instance())

# print(PersonSingleton.get_instance())
# print(PersonSingleton.print_data())