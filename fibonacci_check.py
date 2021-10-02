import math
 
# This will return true if x is perfect square
def isPerfectSquare(x):
    s = int(math.sqrt(x))
    return s*s == x
 
# This will return true if n is a fibinacci number, else false
def isFibonacci(n):
 
    return isPerfectSquare(5*n*n + 4) or isPerfectSquare(5*n*n - 4)
    
# This is to test above functions
for k in range(1,11):
     if (isFibonacci(k) == True):
         print k,"is a Fibonacci Number"
     else:
         print k,"is a not Fibonacci Number "
