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


stu = student('Singh', '20BCS8013')
stu.setAge(10)
stu.setMarks(90)
stu.display()
