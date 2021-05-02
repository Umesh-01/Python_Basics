def func():
  print('this is the simple function.')

func()


def fun(value1, value2):
  if value1<value2:
    print('{value2} is greater than {value1}')
  elif value1==value2:
    print('Both are equal.')
  else:
    print('{value1} is greater than {value2}')

fun(5, 10)
fun(15, 12)
fun(21, 21)


# -------------------Exercise------------------

# class in python

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
