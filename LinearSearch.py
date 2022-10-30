def linear_search(arr, a, b):

    for i in range(0, a):
        if (arr[i] == b):
            return i
    return -1

arr = [9, 7, 5, 3, 1]
print("The array given is ", arr)
b = 5
print("Element to be found is ", b)
a = len(arr)
index = linear_search(arr, a, b)
if(index == -1):
    print("Element is not in the list")
else:
    print("Index of the element is: ", index)
