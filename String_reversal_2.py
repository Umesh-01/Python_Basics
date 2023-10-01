# String reversal using recursion
def reverse(strr):
    if len(strr) == 0:
        return strr
    else:
        return reverse(strr[1:]) + strr[0]
  
strr = "desrever_gnirtS"
  
print ("The original string  is : ",end="")
print (strr)
  
print ("The reversed string(using recursion) is : ",end="")
print (reverse(strr))
