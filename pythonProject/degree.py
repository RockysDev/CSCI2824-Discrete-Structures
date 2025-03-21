class Graph():

	def get_degrees(self, A):
		''' A here is the adjacency matrix '''
		
		#Your code here
		length = len(A)
		ls = []
		for i in range(length):
			indeg = 0
			outdeg = 0
			tuple = ()
			for j in range(length):
				# if A[i][j] == 1:
				indeg = indeg+A[j][i]
				outdeg = outdeg+A[i][j]
			tuple = ()
			tuple = indeg,outdeg
			ls.append(tuple)
		return ls


