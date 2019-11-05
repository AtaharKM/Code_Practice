class Graph:
    def __init__(self, row,col,g):
        self.row=row
        self.col=col
        self.graph=g
        self.visited=[[False for i in range(self.col)]for j in range(self.row)]

    def index_check(self,i,j):
        if (i>=0 and i<self.row):
            if(j>=0 and j<self.col):
                if( not self.visited[i][j]):
                    if self.graph[i][j]:
                        return True

        return False

    def DFS(self,i,j):
        r=[-1,-1,-1,0,0,1,1,1]
        c=[-1,0,1,-1,1,-1,0,1]

        self.visited[i][j]=True

        for k in range(8):
            if self.index_check(i+r[k], j+c[k]):
                self.DFS(i+r[k], j+c[k])

    def countIsland(self):

        count=0
        for i in range(self.row):
            for j in range(self.col):
                if (not self.visited[i][j] ) and self.graph[i][j]:
                    count+=1
                    self.DFS(i,j)
        print('Number of Island is :' , count)


inMat=[[1,1,0,0,0],
       [0,1,1,0,1],
       [1,0,0,1,1],
       [0,0,0,0,1],
       [1,0,1,0,1]]

row=len(inMat)
col=len(inMat[0])

g=Graph(row, col, inMat)

g.countIsland()
