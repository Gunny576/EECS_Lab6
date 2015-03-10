# code to read in the files
# this code is just basic stuff to test how to read in from a csv file
# this code now also checks to make sure the matrix's are valid
import csv
import numpy as np


file1 = open('input1.csv', 'r')  # reads in the first file
file2 = open('input2.csv', 'r')  # reads in the second file

reader1 = csv.reader(file1)
reader2 = csv.reader(file2)

matrix1 = []
matrix2 = []

for line in file1:
    line = [int(x) for x in line.split(',')]
    matrix1.append(line)

for line in file2:
    line = [int(x) for x in line.split(',')]
    matrix2.append(line)


x = matrix1[1][0]+matrix1[1][0]

print(x)
print(matrix1)
print(matrix2)


validFlag1 = 1
validFlag2 = 1

for row in matrix1:
    for row1 in matrix1:
        if len(row) != len(row1):
            validFlag1 = 0

for row in matrix2:
    for row1 in matrix2:
        if len(row) != len(row1):
            validFlag2 = 0

if validFlag1 == 0:
    print("Input from Input1.csv is not a valid Matrix")

if validFlag2 == 0:
    print("Input from Input2.csv is not a valid Matrix")

array1 = np.asarray(matrix1)
array2 = np.asarray(matrix2)

print(array1)
print(array2)