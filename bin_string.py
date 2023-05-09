n = 4
A = [-1]*n
def Try(i):
    for v in range (2):
        A[i] = v
        if i == n-1:
            print(A)
        else:
            Try(i+1)
Try(0)