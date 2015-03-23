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





		
A = [[1,2], [3, 4],[4,4],[5,7]]
B = [[1,2], [3, 4],[4,2],[3,4]]





add_Mat(A,B)
sub_Mat(A,B)
