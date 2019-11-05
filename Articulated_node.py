from collections import defaultdict

class Node:
    def __init__(self,a):
        self.dat=a
        self.color='W'
        self.startTime=0
        self.lowestStartTime=1e9
        self.next=[]
        self.parent=None
        self.finishTime=0

class Graph:
    def __init__(self,V):
        self.vertices=V
        self.graph=[None]*self.vertices
        self.Time=0
        self.AP=[False]*self.vertices

    def addEdge(self, src, dst):
        if self.graph[src]==None:
            n=Node(src)
            self.graph[src]=n
        self.graph[src].next.append(dst)
        if self.graph[dst] == None:
            n = Node(dst)
            self.graph[dst] = n
        self.graph[dst].next.append(src)


    def DFSUtil(self,s):
        self.graph[s].color='G'
        self.Time+=1  #for startTime
        self.graph[s].lowestStartTime=self.Time
        self.graph[s].startTime=self.Time
        for i in self.graph[s].next:
            if(self.graph[i].color=='W'):# Tarjan Algorithm
                self.graph[i].color='G'
                # self.graph[i].startTime=self.Time
                self.graph[i].parent=s
                self.DFSUtil(i)
                self.graph[s].lowestStartTime=min(self.graph[s].lowestStartTime, self.graph[i].lowestStartTime)

                if(self.graph[s].parent!=None and self.graph[s].lowestStartTime>=self.graph[s].startTime):
                   self.AP[s]=True
                if (self.graph[s].parent==None and len(self.graph[s].next)>=2):
                    self.AP[s]=True


            elif(self.graph[i].color=='G' and self.graph[s].parent!=i):
                self.graph[s].lowestStartTime=min(self.graph[s].lowestStartTime, self.graph[i].startTime)

        self.graph[s].color='B'
        # print('\n', s)
        # self.Time += 1 #for Finish Time
        # self.graph[s].finishTime=self.Time

    def DFS(self):
        for i in range(self.vertices):
            if(self.graph[i].color=='W'):
                self.DFSUtil(i)



g1=Graph(10)

g1.addEdge(0, 1)
g1.addEdge(1, 2)
g1.addEdge(2, 3)
g1.addEdge(3, 4)
g1.addEdge(3, 5)
g1.addEdge(3, 7)
g1.addEdge(5, 6)
g1.addEdge(7, 8)
g1.addEdge(0, 8)
g1.addEdge(0, 9)
g1.addEdge(1, 8)

g1.DFS()

print(g1.AP)



