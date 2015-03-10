# code to read in the files
# this code is just basic stuff to test how to read in from a csv file
import csv


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