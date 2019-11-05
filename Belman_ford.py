class Node:
    def __init__(self, dat):
        self.data=dat
        self.parent=None
        self.next=[]
        self.weight=[]
        self.distance=1e9
        self.color='W'

class Graph:
    def __init__(self,V):
        self.vertices=V
        self.graph=[None]*self.vertices

    def addEdge(self,src,dst,weight):
        if(self.graph[src]==None):
            n=Node(src)
            self.graph[src]=n
        if (self.graph[dst] == None):
            n = Node(dst)
            self.graph[dst] = n

        self.graph[src].next.append(dst)
        self.graph[src].weight.append(weight)

    def BFS(self, startPt):
        self.graph[startPt].distance=0
        for k in range(1,self.vertices): #go over all the edge V-1 times
            # print(k)
            for i in range(self.vertices):
                for j in range(len(self.graph[i].next)):
                    v=self.graph[i].next[j]
                    if(self.graph[v].distance>self.graph[i].distance+self.graph[i].weight[j]):
                        self.graph[v].distance =self.graph[i].distance + self.graph[i].weight[j]
                        self.graph[v].parent=i

        for i in range(self.vertices):
            for j in range(len(self.graph[i].next)):
                v=self.graph[i].next[j]
                if(self.graph[v].distance>self.graph[i].distance+self.graph[i].weight[j]):
                    return False
        return True

V=5
g=Graph(V)

g.addEdge(0,1,6)
g.addEdge(0,2,7)
g.addEdge(1,2,8)
g.addEdge(1,3,5)
g.addEdge(2,3,-3)
g.addEdge(2,4,9)
g.addEdge(3,1,-2)
g.addEdge(4,3,7)
g.addEdge(4,0,2)
g.addEdge(1,4,-4)

if(g.BFS(0)):
    print('Shortest Path Available')
else:
    print('Negative cycle present')


