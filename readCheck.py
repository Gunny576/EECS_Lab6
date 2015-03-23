# code to read in the files
# this code is just basic stuff to test how to read in from a csv file
# this code now also checks to make sure the matrix's are valid
import csv
import numpy as np

file1 = 'input1.csv'
file2 = 'input2.csv'

def fileReader(filename):
    file1Open = open(filename, 'r')
    
    reader1 = csv.reader(file1Open)

    matrix1 = []

    for line in file1Open:
        line = [int(x) for x in line.split(',')]
        matrix1.append(line)
        array = np.asarray(matrix1)
    print(array)
    return array


def matrixValidator(matrix):
    validFlag = True
    for row in matrix:
        for row1 in matrix:
            if len(row) != len(row1):
               validFlag1 = False
    
    if(validFlag == True):
        print("Matrix is valid.")
    if(validFlag == False):
        print("Matrix is invalid")

    return validFlag




def transpose(matrix):
    TransposeMatrix = [ [ 0 for a in range(len(matrix[0]))]for b in range (len(matrix))]
    for i in range (len(matrix)):
        for j in range (len(matrix[0])):
            TransposeMatrix[j][i] = matrix[i][j]
    print TransposeMatrix    
    return TransposeMatrix
    
    

def add_Mat(mat_a,mat_b) :
	
	a = len(mat_a)
	b = len(mat_a[0])
	c = len(mat_b)
	d = len(mat_b[0])
	if a == c and b == d:
		
		mat_Result = [ [ 0 for r in range(b) ] for s in range(a) ]
				
				
		for i in range (a):
			for j in range (b):
				mat_Result[i][j] = mat_a[i][j] + mat_b[i][j]
						
				
				
		print mat_Result
		

	else:
		print "Matrices don't have same rows or columns"
		

def sub_Mat(mat_a,mat_b) :

	a = len(mat_a)
	b = len(mat_a[0])
	c = len(mat_b)
	d = len(mat_b[0])
	
	if a == c and b == d:

		mat_Result = [ [ 0 for r in range(b) ] for s in range(a) ]


		for i in range (a):
			for j in range (b):
				mat_Result[i][j] = mat_a[i][j] * -1 + mat_b[i][j]
      
      		 

		print mat_Result

	else:
		print "Matrices don't have same rows or columns"
		
		
def mult(a,b):
	rowa = len(a)
	cola = len(a[0])
	rowb = len(b)
	colb = len(b[0])
	if cola == rowb:
		print('Running')
		result = [ [ 0 for r in range(colb) ] for s in range(rowa) ]
		for i in range(len(a)):
  			for j in range(len(b[0])):
      				 for k in range(len(b)):
           				result[i][j] += a[i][k] * b[k][j]
		print result








array1 = fileReader(file1)
array2 = fileReader(file2)




matrixValidator(array1)
matrixValidator(array2)

print "Try to add matrices"

add_Mat(array1,array2)

print "Try to subtract matrices"

sub_Mat(array1,array2)

print "Try to multiply matrices"

mult(array1,array2)

print "Transpose matrix 1"

transpose(array1)

print  "Transpose matrix 2"

transpose(array2)

