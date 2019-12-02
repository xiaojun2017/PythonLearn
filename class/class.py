class Person:
    def say_hi(self):
        print('Hello, class hello world')
        print('Person : ', self.names, self.ages)

    def __init__(self, name, age):
        self.names = name
        self.ages = age

    pass


p = Person('John', '25')
print(p)

p.say_hi()
