# Program to check whether a string is palindrome or not
 
def isPalindrome(strp):
    return strp == strp[::-1]
 
 
# Driver code
strp = input("Enter String ")
ans = isPalindrome(strp)
 
if ans:
    print("Yes")
else:
    print("No")
