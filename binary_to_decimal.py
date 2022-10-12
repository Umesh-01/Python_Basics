while True:
    try:
        temp = int(input('Binary num: '))
        binary = temp
        while temp > 0:
            if temp % 10 != 0 and temp % 10 != 1:
                raise
            temp //= 10
        break
    except:
        print('Invalid Binary Number!')
        pass

decimal = 0
position = 0
while binary > 0:
    digit = binary % 10
    decimal += digit * (2**position)
    binary //= 10
    position += 1
print(decimal)
