
class Room:
    
    def __init__(self, id: str, floor: int, seats: int):
        self.id: str = id
        self.floor: int = floor
        self.seats: int = seats
        self.area: float = 2 * self.seats
        
    def get_floor(self) -> int:
        return self.floor
    
    def get_seats(self) -> int:
        return self.seats
    
    def get_id(self) -> str:
        return self.id
    
    def get_area(self) -> float:
        return self.area
        
    def __str__(self) -> str:
        return f'Room(id={self.get_id()}, floor={self.get_floor()}, seats={self.get_seats()})'

class Building:
    
    def __init__(self, name: str, address: str, floors: tuple[int, int]):
        self.name: str = name
        self.address: str = address
        self.floors: int = floors
        self.rooms: list[Room] = []
        
    def get_floors(self) -> tuple[int, int]:
        return self.floors
    
    def get_rooms(self) -> list[Room]:
        return self.rooms
        
    def add_room(self, room: Room):
        floors = self.get_floors()
        if room and isinstance(room, Room) and room not in self.rooms\
            and floors[0] <= room.get_floor() <= floors[1]:
            self.rooms.append(room)
            
    def area(self) -> float:
        sum_area: float = 0
        for room in self.rooms:
            sum_area += room.get_area()
        return sum_area
        
    def __str__(self) -> str:
        s: str = f'{self.name} @ {self.address}\n'
        s += "With Rooms:\n"
        for room in self.get_rooms():
            s += room.__str__() + "\n"
        return s + f'Area = {self.area()}m2'
    
class Person:
    
    def __init__(self, cf: str, name: str, surname: str, age: int):
        self.cf: str = cf
        self.name: str = name
        self.surname: str = surname
        self.age: int = age
        
    def __str__(self) -> str:
        return f'{self.__class__.__name__}(cf={self.cf}, name={self.name}, surname={self.surname}, age={self.age})'
    
class Student(Person):
    
    def __init__(self, cf: str, name: str, surname: str, age: int):
        super().__init__(cf, name, surname, age)
        self.group: Group = None
        
    def set_group(self, group):
        self.group = group
        
class Lecturer(Person):
    
    def __init__(self, cf: str, name: str, surname: str, age: int):
        super().__init__(cf, name, surname, age)
    
class Group:
    
    def __init__(self, name: str, limit: int):
        self.name: str = name
        self.limit: int = limit
        self.students: list[Student] = []
        self.lecturers: list[Lecturer] = []
        
    def get_name(self) -> str:
        return self.name
    
    def get_limit(self) -> int:
        return self.limit
    
    def get_students(self) -> list[Student]:
        return self.students
    
    def get_limit_lecturers(self):
        return max(len(self.students) // 10, 1)
    
    def add_student(self, student: Student) -> bool:
        limit: int = self.get_limit()
        if student and isinstance(student, Student)\
            and student not in self.students and limit > 0:
            self.students.append(student)
            student.set_group(self)
            self.limit -= 1
            return True
        return False
            
    def add_lecturer(self, lecturer: Lecturer):
        if lecturer and isinstance(lecturer, Lecturer)\
            and lecturer not in self.lecturers and self.get_limit_lecturers() > len(self.lecturers):
                self.lecturers.append(lecturer)
                
class Course:
    
    def __init__(self, name: str):
        self.name: str = name
        self.groups: list[Group] = []
        
    def register(self, student: Student):
        for group in self.get_groups():
            if group.add_student(student):
                break
        
    def get_groups(self) -> list[Group]:
        return self.groups
        
    def add_group(self, group: Group):
        if group and isinstance(group, Group)\
            and group not in self.groups:
            self.groups.append(group)
        
    
smi = Building(name="SMI", address="Via Sierra Nevada 60", floors=[-2,3])
armellini = Building(name="ITIS", address="Basilica San Paolo", floors=[0,4])

smi.add_room(Room(id="666", floor=3, seats=32))
smi.add_room(Room(id="333", floor=0, seats=42))
smi.add_room(Room(id="111", floor=6, seats=32))
smi.add_room(Room(id="111", floor=-1, seats=32))

fullstack = Group(name="Fullstack", limit=1)
cloud = Group(name="cloud", limit=10)
cyber = Group(name="cyber", limit=10)

course = Course(name="Python")
course.add_group(fullstack)
course.add_group(cloud)
course.add_group(cyber)
course.register(Student(cf="1234", name="Flavio", surname="Maggi", age=29))
course.register(Student(cf="1234", name="Toni", surname="Mancini", age=46))
course.register(Student(cf="1234", name="Toni", surname="Mancini", age=46))
print(f'Studenti in fullstack: {len(course.groups[0].students)}')
print(f'Studenti in cloud: {len(course.groups[1].students)}')