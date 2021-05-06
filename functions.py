# function exercises

# 1st Greeter

def fun_greet(name):
    print(f"Hello!! {name}.")
    print(f"How are u {name}??")
    print(f"I hope everything is fine, {name}.\n")


names = ['Umesh', 'Singh', 'GitHub']
for name in names:
    fun_greet(name)

# 2nd Full names

def full_name(f_name, l_name):
    print(f"Hello!! {f_name} {l_name}.\n")


full_name('Umesh', 'Singh')
full_name('Git', 'Hub')
full_name('Python', 'Programming')

# 3rd Addition Calculator

def sum(num1, num2):
    print(f"Sum of {num1} and {num2} is {num1+num2}.\n")

sum(7, 5)
sum(15, 21)
sum(35, 71)

# 4th Return Calculator

def sum(num1, num2):
    return num1+num2

num1 = 11
num2 = 10
print(f"Sum of {num1} and {num2} is {sum(num1,num2)}")



# -----------------------------------------------
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
