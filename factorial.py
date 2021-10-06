# Python program to calculate the factorial of a number using recursion
def fact(n):
    if n<=1:
        return 1
    return n * fact(n-1)

if __name__ == '__main__':
    num = int(input("Please Enter the Number: "))
    f = fact(num)
    print(f"The Factorial of {num} is {f}")