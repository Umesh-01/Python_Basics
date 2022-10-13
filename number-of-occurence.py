#Python program to count number of occurences of a number in an array

#Prompt user for array
array_num = list(map(int, input("\nEnter array elements: ").split()))

#Prompt for number to be searched
num=int(input("\nNumber to be searched: "))

#Print number of occurences
print("\nNumber of occurrences of the",num,"in the array: "+str(array_num.count(num)))
