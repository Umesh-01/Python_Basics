# Python3 program to sort a given matrix

SIZE = 10

def sortMat(mat, n) :
	
	# Temporary matrix of size n^2
	temp = [0] * (n * n)
	k = 0

	# Copy the elements of the matrix into temp[]
	for i in range(0, n) :
		for j in range(0, n) :
			temp[k] = mat[i][j]
			k += 1

	# sort temp[]
	temp.sort()
	
	# copy the elements of temp[] into mat[][]
	k = 0
	
	for i in range(0, n) :
		for j in range(0, n) :
			mat[i][j] = temp[k]
			k += 1

def printMat(mat, n) :
	
	for i in range(0, n) :
		for j in range( 0, n ) :
			print(mat[i][j] , end = " ")
			
		print()
	
	
# Test Case
mat = [ [ 5, 4, 7 ],
		[ 1, 3, 8 ],
		[ 2, 9, 6 ] ]
n = 3

print( "Given Matrix:")
printMat(mat, n)

sortMat(mat, n)

print("\nSorted Matrix: ")
printMat(mat, n)
