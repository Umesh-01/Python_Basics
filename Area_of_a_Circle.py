# Taking diameter from user
diameter = float(input("Enter the diameter of circle : "))

# Taking diameter measure unit from user
unit = input("Enter the measure unit of diameter (e.g. in, cm) : ")

# Finding area of a circle using ( A = 1/4 * /\ * D*D ) formula
area = ((1 / 4) * (22 / 7) * (diameter * diameter))

# Printing the area
print("Area of circle is : ",area,unit+"2")
