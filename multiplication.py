from numpy  import *

def mult(a,b):
	rowa = a.itemsize + 1
	cola = a.ndim +1
	rowb = b.itemsize + 1
	colb = b.ndim +1
	if cola == rowb:
		print('Running')
		result = zeros( (rowa,colb) )
		for i in range(len(a)):
  			for j in range(len(b[0])):
      				 for k in range(len(b)):
           				result[i][j] += a[i][k] * b[k][j]
		print(result)
		



