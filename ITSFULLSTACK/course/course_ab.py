from group import Group
from people.student import Student
from abc import ABC, abstractclassmethod

class CourseAB(ABC):

    def __init__(self, name:str):
        self.name: str = name
        self.groups: list[Group] = []

    @abstractclassmethod
    def register_student(self, student: Student):
        pass

    def add_group