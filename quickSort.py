array=[]

def quickSort(arr,piv):
    left=[]
    right=[]

    for i in arr:
        if(i>piv):
            right.append(i)
        else:
            left.append(i)

    if (len(left)>=1):
        quickSort(left, left[0])
    if(len(right)>=1):
        quickSort(right,right[0])

    array.__add__(left,right)


a=[1,2,3,4,-1,0,-5,-7,1,2,-100,100]
quickSort(a,a[0])
