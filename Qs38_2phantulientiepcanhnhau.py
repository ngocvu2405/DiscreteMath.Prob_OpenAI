import operator as op
from functools import reduce

def ncr(n, r):
    r = min(r, n-r)
    numer = reduce(op.mul, range(n, n-r, -1), 1)
    denom = reduce(op.mul, range(1, r+1), 1)
    return numer // denom


def F(k,n):
	if k == 0 or k == n:
		return 1
	elif k > n or k <= 1 or n <= 1:
		return 0
	else:
		return F(k-1,n-2) + ncr(n-2,k-2) + F(k,n-1)

print(F(5,11))