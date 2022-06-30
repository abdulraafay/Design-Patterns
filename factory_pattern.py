from abc import ABCMeta, abstractstaticmethod
from os import stat

class IPerson(metaclass=ABCMeta):
    
    @abstractstaticmethod
    def person_method():
        pass

class Teacher(IPerson):
    
    @staticmethod
    def person_method():
        print('I am a teacher')

class Student(IPerson):
    
    @staticmethod
    def person_method():
        print('I am a student')

class PersonFactory:
    
    @staticmethod
    def factory(type):
        if (type == 'Student'):
            return Student()
        if (type == 'Teacher'):
            return Teacher()
        return 'Incorrect type provided'


if __name__ == '__main__':

    type = input('What type of person do you want to create?')

    person = PersonFactory.factory(type)
    if (isinstance(person, str)):
        print(person)
    else:
        person.person_method()    