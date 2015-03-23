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


array1 = fileReader(file1)
array2 = fileReader(file2)


def transpose(matrix):
    TransposeMatrix = [ [ 0 for a in range(len(matrix[0]))]for b in range (len(matrix))]
    for i in range (len(matrix)):
        for j in range (len(matrix[0])):
            TransposeMatrix[j][i] = matrix[i][j]
    print(TransposeMatrix)    
    return TransposeMatrix

