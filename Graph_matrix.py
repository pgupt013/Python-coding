class Graph:
    def __init__(self,size):
        self.matrix=[]
        for i in range(size):
            self.matrix.append([0 for j in range(size)])
            #for j in range(size):
             #   self.matrix.append[0]

    def add_edge(self, v1, v2):
	    if v1 == v2:
		    print("Both vertices are same")
		    return
	    self.matrix[v1][v2] = 1
	    self.matrix[v2][v1] = 1
    
    def print_matrix(self):
	    for row in self.matrix:
		    print(row)

g=Graph(4)
g.add_edge(0, 1)
g.add_edge(1, 2)
g.add_edge(0, 2)
g.add_edge(2, 3)
g.print_matrix()