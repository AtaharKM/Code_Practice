from copy import deepcopy
def floydWalsh(W):
    n=len(W)
    Dk_1=W
    for k in range(n):
        Dk=[[None]*n,[None]*n,[None]*n,[None]*n,[None]*n,[None]*n]
        for i in range(n):
            for j in range(n):
                Dk[i][j]=min(Dk_1[i][j],Dk_1[i][k]+Dk_1[k][j])

        print(Dk)
        print('\n')
        Dk_1=deepcopy(Dk)
    return Dk_1

# W=[[0,3,8,1e9,-4],[1e9,0,1e9,1,7],[1e9,4,0,1e9,1e9],[2,1e9,-5,0,1e9],[1e9,1e9,1e9,6,0]]
W=[[0,3,8,1e9,-4,1e9],[1e9,0,1e9,1,7,1e9],[1e9,4,0,1e9,1e9,1e9],[2,1e9,-5,0,1e9,1e9],[1e9,1e9,1e9,6,0,4],[1e9,1e9,1e9,1,1e9,0]]

print(floydWalsh(W))
