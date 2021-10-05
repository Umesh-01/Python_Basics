# Python code to reverse a string 
# using loop
  
def reverse(s):
  str = ""
  for i in s:
    str = i + str
  return str
  
strm = "desrever_gnirtS"
  
print ("The original string  is : ",end="")
print (strm)
  
print ("The reversed string(using loops) is : ",end="")
print (reverse(strm))
