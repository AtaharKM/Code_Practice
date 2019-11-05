# Python3 Program to print BFS traversal 
# from a given source vertex. BFS(int s) 
# traverses vertices reachable from s. 
from collections import defaultdict 

class node:
    def __init__(self):
        self.dat=None
        self.next=[]
        self.color='W'
        self.weight=None
        self.parent=None
        self.distance=None

# This class represents a directed graph 
# using adjacency list representation 
class Graph: 
	# Constructor
    def __init__(self,V):
        self.vertex=V
        self.graph=[None]* self.vertex
        for i in range(self.vertex):
            N=node()
            self.graph[i]=N

    # function to add an edge to graph
    def addEdge(self,src,dest):
       self.graph[src].next.append(dest)

    # Function to print a BFS of graph
    def BFS(self, s):
        self.graph[s].color='G'
        self.graph[s].distance=0
        self.parent=None
        que=[]
        que.append(s)

        while que:
            u=que.pop(0)
            print(u, end=' ')

            for i in self.graph[u].next:
                if self.graph[i].color=='W':
                    self.graph[i].color='G'
                    self.graph[i].distance=1+self.graph[u].distance
                    self.graph[i].parent=u
                    que.append(i)
            self.graph[u].color='B'


# Driver code 

# Create a graph given in 
# the above diagram 
g = Graph(4)
g.addEdge(0, 1) 
g.addEdge(0, 2) 
g.addEdge(1, 2) 
g.addEdge(2, 0) 
g.addEdge(2, 3) 
g.addEdge(3, 3) 
#
# print ("Following is Breadth First Traversal"
# 				" (starting from vertex 2)")
g.BFS(3)

