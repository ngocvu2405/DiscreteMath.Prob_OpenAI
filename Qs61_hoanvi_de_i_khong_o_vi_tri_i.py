
#hoán vị 5 phần tử để nó ko còn ở vị trí của nó
def F(n):
    if n ==0:
        return 1
    elif n <0:
        return 0
    else:
        return (n-1)*(F(n-1)+F(n-2))

print(F(5))