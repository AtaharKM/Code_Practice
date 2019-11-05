class Node:
    def __init__(self,dat):
        self.data=dat
        self.next=[]
        self.color='W'
        self.weight=[]
        self.parent=None
        self.start_time=None
        self.finish_time=None
        self.distance=0

class Graph:
    def __init__(self,V):
        self.vertices=V
        self.graph=[None]*V
        self.MaxLength=0

    def addEdge(self,src,dst,weight):
        if(self.graph[src]==None):
            n=Node(src)
            # n.weight=weight
            self.graph[src]=n
        if (self.graph[dst] == None):
            n = Node(dst)
            self.graph[dst] = n
        self.graph[src].next.append(dst)
        self.graph[src].weight.append(weight)

    def DFSHelper(self,startNode):
        if(self.graph[startNode].color=='W'):
            self.graph[startNode].color = 'G'

        for i in range(len(self.graph[startNode].next)):
            s=self.graph[startNode].next[i]
            if (self.graph[s] != None):
                if (self.graph[s].color == 'W'):
                    self.graph[s].parent=startNode
                    self.graph[s].distance=self.graph[startNode].weight[i]+self.graph[startNode].distance
                    if(self.MaxLength<self.graph[s].distance):
                        self.MaxLength=self.graph[s].distance
                    self.DFSHelper(s)
        self.graph[startNode].color='B'

    def DFS(self):
        for i in range(self.vertices):
            if(self.graph[i]!=None):
                if (self.graph[i].color == 'W'):

                    self.DFSHelper(i)



g=Graph(6)
g.addEdge(0,1,3)
g.addEdge(1,2,4)
g.addEdge(1,5,2)
g.addEdge(5,3,6)
g.addEdge(5,4,5)

g.DFS()
