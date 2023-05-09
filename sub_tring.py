n = 5
m = 3
A = [-1]*m
arr=[]
k = m*(m+1)/2

def Try(i):
    lb = 0
    if i>0:
        lb = A[i-1] +1
    ub = n-m+i
    for v in range (lb, ub+1):
        A[i] = v
        if i == m -1:
            print(A)
        else:
            Try(i+1)
Try(0)