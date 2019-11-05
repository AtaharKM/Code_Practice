class Node:
    def __init__(self, dat):
        self.dat=dat
        self.parent=None
        self.distance=1e9
        self.weight=[]
        self.next=[]
        self.color='W'
        self.startTime=0
        self.FinishTime=0

class Graph:
    def __init__(self,V):
        self.vertices=V
        self.graph=[None]*self.vertices
        self.Time=0
        self.stk=[]

    def addEdge(self,src,dst, weight):
        if (self.graph[src]==None):
            n=Node(src)
            self.graph[src]=n
        if(self.graph[dst]==None):
            n=Node(dst)
            self.graph[dst]=n
        self.graph[src].next.append(dst)
        self.graph[src].weight.append(weight)

    def DFSUtil(self,s):
        self.graph[s].color='G'
        self.Time+=1
        self.graph[s].startTime=self.Time

        for i in self.graph[s].next:
            if(self.graph[i].color=='W'):
                self.graph[i].parent=s
                self.DFSUtil(i)
        self.graph[s].color='B'
        self.Time+=1
        self.graph[s].finishTime=self.Time
        self.stk.append(s)
        print(s,'\n')

    def DFS(self):
        for i in range(self.vertices):
            if(self.graph[i].color=='W'):
                self.DFSUtil(i)

    def singleSourceShortestPath(self, s):
        self.graph[s].distance=0
        while self.stk:
            u=self.stk.pop()
            for i in range(len(self.graph[u].next)):
                v=self.graph[u].next[i]
                if(self.graph[v].distance> self.graph[u].distance+self.graph[u].weight[i]):#Relax
                    self.graph[v].distance = self.graph[u].distance + self.graph[u].weight[i]
                    self.graph[v].parent=u



g = Graph(6)
g.addEdge(0, 1,5)
g.addEdge(0, 2,3)
g.addEdge(1, 2,2)
g.addEdge(1, 3,6)
g.addEdge(2, 3,7)
g.addEdge(2, 4,4)
g.addEdge(2, 5,2)
g.addEdge(3, 4,-1)
g.addEdge(3, 5,1)
g.addEdge(4, 5,-2)

g.DFS()
g.singleSourceShortestPath(1)
