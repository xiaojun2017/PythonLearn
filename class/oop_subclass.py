# coding=UTF-8
class SchoolMember:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def tell(self):
        print("Tell, {} {}".format(self.name, self.age))


class Teacher(SchoolMember):
    def __init__(self, name, age, salary):
        SchoolMember.__init__(self, name, age)
        self.salary = salary
        print('Init Teacher : {}'.format(name))

    def tell(self):
        SchoolMember.tell(self)
        print('salary: {:d}'.format(self.salary))


class Student(SchoolMember):
    def __init__(self, name, age, marks):
        SchoolMember.__init__(self, name, age)
        self.marks = marks
        print('Init Student :{}'.format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print('Marks: "{}"'.format(self.marks))


t = Teacher('MrLock', 30, 30000)
s = Student('Xiaoming', 22, 'Good Boy')

print()
members = [t, s]

for m in members:
    m.tell()
