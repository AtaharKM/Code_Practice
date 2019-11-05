# Python3 Program to print BFS traversal
# from a given source vertex. BFS(int s)
# traverses vertices reachable from s.
from collections import defaultdict

class Node:
    def __init__(self,src):
        self.dat=src
        self.next=[]
        self.color='W'
        self.weight=[]
        self.parent=None
        self.distance=1e9

# This class represents a directed graph
# using adjacency list representation
class Graph:
	# Constructor
    def __init__(self,V):
        self.vertex=V
        self.graph=[None]* self.vertex

    # function to add an edge to graph
    def addEdge(self,src,dst,weight):


        if (self.graph[src] == None):
            n = Node(src)
            # n.weight=weight
            self.graph[src] = n
        if (self.graph[dst] == None):
            n = Node(dst)
            self.graph[dst] = n
        self.graph[src].next.append(dst)
        self.graph[src].weight.append(weight)

    # Function to print a BFS of graph
    def BFS(self, s, dest):
        self.graph[s].color='G'
        self.graph[s].distance=0
        # self.parent=None
        que=[]
        que.append(s)
        # que=self.bubbleSort(que)

        while que:
            if(self.graph[dest].color=='B'):
                break
            u=que.pop(0)
            print(u, end=' ')

            for i in range(len(self.graph[u].next)):
                k=self.graph[u].next[i]
                if k!=s:
                    # self.graph[k].color='G'
                    #Relaxation
                    if(self.graph[k].distance>self.graph[u].weight[i]+self.graph[u].distance):
                        self.graph[k].distance=self.graph[u].weight[i]+self.graph[u].distance
                        self.graph[k].parent=u
                        # if(k== dest):
                        #     break
                        if(not que.__contains__(k)):
                            que.append(k)
                            que = self.bubbleSort(que)
            self.graph[u].color='B'

    def bubbleSort(self,s):
        for i in range(len(s)):
            for j in range(i, 0, -1):
                if(self.graph[s[j]].distance <self.graph[s[j-1]].distance):
                    tem=s[j]
                    s[j]=s[j-1]
                    s[j-1]=tem
        return s


# Driver code

# Create a graph given in
# the above diagram
g = Graph(7)
g.addEdge(0, 1,4)
g.addEdge(0, 2,5)
g.addEdge(0, 3,3)
g.addEdge(1, 4,2)
g.addEdge(2, 5,5)
g.addEdge(2, 6,3)
g.addEdge(4, 5,2)
g.addEdge(3, 5,11)
g.addEdge(5, 6,1)
g.addEdge(6, 2,1) #?????
g.addEdge(5, 0,1) #?????
g.addEdge(6, 5,2) #?????
#
dest=5
# print ("Following is Breadth First Traversal"
# 				" (starting from vertex 2)")
g.BFS(0,dest)
#
print("\n Shortest Path from Source to dest \n ", dest)
while dest:
    print(' ',g.graph[dest].parent)
    dest=g.graph[dest].parent

