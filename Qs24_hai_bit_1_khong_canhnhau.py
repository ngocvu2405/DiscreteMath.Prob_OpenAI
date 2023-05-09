def F(n):
    if n == 0:
        return 1
    elif n == 1:
        return 2
    else:
        return F(n-1)+F(n-2)

print(F(6))