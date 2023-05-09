n = 3
A =[-1]*n
mark = [True]*n

def Try(k):
    for j in range(n):
        if mark[j]:
            A[k] = j
            mark[j] = False
            if k == n-1:
                print(A)
            else:
                Try(k+1)
            mark[j] = True
Try(0)



