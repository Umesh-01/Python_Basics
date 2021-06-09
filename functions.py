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

#filter function
def fun1(a):
    return a%2==0
l=[2,5,6,23,34,68,12]
f1=filter(fun1,l)
print(f1,type(f1))
print(list(f1))#we can make use of filter only once
l1=list(f1)
print(l1)#we will get null

#lambda function
v4=lambda x:x%2==0
f2=filter(f4,l)
for i in f2:
    print(i)

def fun1(a):
    return a**3
print()
print(fun1(3))
print(fun1(5))
v2=lambda x,y:x+y
print()
print(v2(2,7))

v3=lambda x,y:x if x>y else y
print()
print(v3(4,8))
print(v3(6,3))

#map function
l=[1,2,3,4,5,6,7]
def fun2(a):
    return a*a

m1=map(fun2,l)
print(list(m1),type(m1))

v=lambda x:x*x
m2=map(v5,l)
print(m2,list(m2),type(m1))
#reduce function
#reduces the sequence of elements into a single value
#reduce will be imported from functools
from functools import *
l=[1,2,3,4,5,6,7]
def fun3(a,b):
    return a+b
r3= reduce(fun3,l)
print(r3)

v6=lambda x,y:x+y
r4=reduce(v6,l)
print(r4)
