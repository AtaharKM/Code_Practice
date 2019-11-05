class Node:
    def __init__(self,dat):
        self.data=dat
        self.next=[]
        self.color='W'
        self.weight=None
        self.parent=None
        self.start_time=None
        self.finish_time=None

class Graph:
    def __init__(self,V):
        self.graph=[None]*V
        self.stk=[] # This will give topological sort
        self.D=0
    def addEdge(self,src,dest):
        if(self.graph[src]==None):
            node=Node(src)
            self.graph[src]=node
        if(self.graph[dest]==None):
            node = Node(dest)
            self.graph[dest] = node

        self.graph[src].next.append(dest)

    def helperDFS(self, startNode):
        print(startNode, end=' ')
        self.D=self.D+1
        self.graph[startNode].start_time=self.D
        self.graph[startNode].color='G'
        for j in self.graph[startNode].next:
            if(self.graph[j].color=='W'):
                self.graph[j].parent=startNode
                self.helperDFS(j)

        self.graph[startNode].color='B'
        self.stk.append(startNode)
        self.D=1+self.D
        self.graph[startNode].finish_time=self.D

    def DFS(self):
        for start in range(len(self.graph)):
            if self.graph[start].color=='W':
                self.helperDFS(start)



def searchPath(gra,src,dest):
    path=[]
    path.append(dest)
    temp=gra[dest].parent
    path.append(temp)
    while temp!=src:
        path.append(gra[temp].parent)
        temp=gra[temp].parent
    return path

def graph_T(gra):
    L=len(g.graph)
    g_t=Graph(L)
    for i in range(L):
        for j in gra.graph[i].next:
            g_t.addEdge(j,i)
    return g_t


# Create a graph given in
# the above diagram
g = Graph(5)
g.addEdge(0, 2)
g.addEdge(0, 3)
g.addEdge(2, 1)
g.addEdge(1, 0)
g.addEdge(3, 4)

#
# print ("Following is Breadth First Traversal"
# 				" (starting from vertex 2)")
g.DFS()


#Strongly connected components
g_T=graph_T(g)

print('\n')

while g.stk:
    i=g.stk.pop()
    if g_T.graph[i].color=='W':
        print('New Node= ', i)
        g_T.helperDFS(i)
        print('\n')

# g_T.DFS()



# print(searchPath(g.graph, 0,3))
