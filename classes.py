# definition of a class named as Student
class student():
    def __init__(self, name, rollno):
        self.name = name
        self.roll = rollno

    def setAge(self, age):
        self.age = age

    def setMarks(self, marks):
        self.marks = marks

    def display(self):
        print('Student details-')
        print('Name-', self.name)
        print('Roll no.-', self.roll)
        print('Age-', self.age)
        print('Marks-', self.marks)


# creating an object for class student        
stu = student('Singh', '20BCS8013')

# calling different methods of class using its object
stu.setAge(10)
stu.setMarks(90)
stu.display()

# classes exercise

# rocket with no class
class Rocket():
    def __init__(self):
        self.x = 0
        self.y = 0

    def move_up(self):
        self.y += 1
        self.x += 1


rocket = [Rocket() for i in range(0, 5)]
print(rocket.y)
print(rocket[1].move_up())
