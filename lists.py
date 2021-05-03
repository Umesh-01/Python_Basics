# lists in python

names = ['singh', 'umesh', 'git', 'github']
print(names[1])

print(names[1].title())

for name in names:
    print(name)
  
for name in names:
    print('I am'+name+'.')
  
for index, name in enumerate(names):
    indx = str(index)
    print("Index No.: " + indx + " Name: " + name.title())
   

names.append('open-source')

print(names)

names.insert(3,'hacktoberfest')

print(names)
