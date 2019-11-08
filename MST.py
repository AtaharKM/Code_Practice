class Edge:
    def __init__(self, src,dst,weight):
        self.src=src
        self.dst=dst
        self.weight=weight
        self.disjoint=True

class Graph:
    def __init__(self,V):
        self.vertices=V
        self.mst=[]
        self.edge=[]
        self.set=[[i] for i in range(self.vertices)]

    def addEdge(self,src,dst,weight):
        E=Edge(src,dst,weight)
        self.edge.append(E)

    def sortEdge(self,edgeNum):
        for i in range(1,edgeNum):

            for j in range(i-1,-1,-1):
                if(self.edge[j+1].weight<self.edge[j].weight):
                    tmp = self.edge[j+1]
                    self.edge[j+1]=self.edge[j]
                    self.edge[j]=tmp

    def Find(self,x):
        L=len(self.set)
        for i in range(L):
            if(self.set[i].__contains__(x)):
                return i
    def Union(self,sI,dI):
        self.set[sI]=self.set[sI].__add__(self.set[dI])
        self.set.remove(self.set[dI])

    def MST(self):
        for i in self.edge:
            sI=self.Find(i.src)
            dI=self.Find(i.dst)
            if(sI!=dI):
                self.Union(sI,dI)
                self.mst.append(i)



g=Graph(5)

g.addEdge(0,1,1)
g.addEdge(1,2,5)
g.addEdge(1,3,4)
g.addEdge(1,4,3)
g.addEdge(3,4,2)
g.addEdge(2,3,6)
g.addEdge(2,0,7)

g.sortEdge(7)
g.MST()






