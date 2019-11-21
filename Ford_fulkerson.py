class Node:
    def __init__(self,src):
        self.dat=src
        self.weight=[]
        self.next=[]
        self.parent=-1
        self.residual=[]
        self.color='W'

class E:
    def __init__(self,src,dst,weight):
        self.src=src
        self.dst=dst
        self.weight=weight

class Graph:

    def __init__(self,V):
        self.vertices=V
        self.g=[None]*self.vertices
        self.que=[]
        # self.Edge=[]
        self.maxFlow=0

    def addEdge(self,src,dst, weight):
        if(self.g[src]==None):
            self.g[src]=Node(src)
        if(self.g[dst]==None):
            self.g[dst]=Node(dst)
        self.g[src].weight.append(weight)
        self.g[src].next.append(dst)
        self.g[src].residual.append(0)


    def BFS(self,Start,End ):
        self.que.append(Start)
        self.g[Start].color='B'
        while self.que:
            p=self.que.pop(0)
            # print(p)
            for i in range(len(self.g[p].next)):

                s=self.g[p].next[i]
                W=self.g[p].weight[i]

                if(self.g[s].color=='W' and W):
                    self.g[s].color='G'
                    self.que.append(s)
                    self.g[s].parent=p
                    if(s==End):
                        # break
                        self.GetPath(End)
                        self.resetGraph()
                        self.BFS(Start,End)
                        return

            # if (s == End):
            #     break
            self.g[p].color='B'

    def getIndex(self,lst,index):
        for i in range(len(lst)):
            if lst[i]==index:
                return i

    def resetGraph(self):
        for i in self.g:
            i.color='W'
        self.que=[]

    def GetPath(self,End):
        MinFlow=1e9
        s=self.g[End]
        p=s.parent
        while (p>=0):
            print(p)
            MinFlow=min(MinFlow,self.g[p].weight[self.getIndex(self.g[p].next,s.dat)])
            s=self.g[p]
            p=s.parent

        self.maxFlow+=MinFlow

        s = self.g[End]
        p = s.parent
        while (p >= 0):
            # print(p)
            self.g[p].weight[self.getIndex(self.g[p].next, s.dat)]-=MinFlow
            s = self.g[p]
            p = s.parent







g=Graph(6)
g.addEdge(0,1,16)
g.addEdge(1,3,12)
g.addEdge(3,5,20)
g.addEdge(0,2,13)
g.addEdge(2,4,14)
g.addEdge(1,2,10)
g.addEdge(2,1,4)
g.addEdge(4,5,4)
g.addEdge(4,3,7)
g.addEdge(3,2,9)

g.BFS(0,5)

# g.GetPath(5)








