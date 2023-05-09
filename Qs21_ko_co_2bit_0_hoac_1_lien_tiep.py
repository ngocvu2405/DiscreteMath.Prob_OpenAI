c =0
def Count(n):
    if n !=1:
        return 2*Count2(n-1)+Count(n-1)
    else:
        res = 3
        return res
def Count2(n):
    if n != 1:
        return Count(n-1)+Count2(n-1)
    else:
        res =2
        return res

n = int(input())
print(Count(n))