def add_Mat(mat_a,mat_b) :
	
	a = len(mat_a)
	c = len(mat_a[0])
	b = len(mat_b)
	d = len(mat_b[0])
	if a == b and c == d:
		
		C = [ [ 0 for r in range(c) ] for s in range(a) ]
				
				
		for i in range(len(A)):
			for j in range(len(A[0])):
				result = A[i][j] + B[i][j]
						
				C[i][j] = (result)
				
		print C

	else:
		print "Matrices don't have same rows or columns"
		
		
A = [[1,2], [3, 4],[2,4],[5,7]]
B = [[1,2], [3, 4],[1,2],[3,4]]


add_Mat(A,B)