A = [1, 3, 2, 7, 6, 8, 4, 2, 6, 7]
# s_sub = []
s_odd= []
s_even = []
def sum_substring(k):
    # A = [1, 3, 2, 7, 6, 8, 4, 2, 6, 7]
    s_sub = []
    # s_odd= []
    # s_even = []
    for i in range(k):
        Si = 0
        for j in range (i,k):
            Si = Si + A[j]
            # print(Si)
        s_sub.append(Si)
    # print(s_sub)
    for ele in s_sub:
        if ele %2 == 0:
            s_even.append(ele)
        else:
            s_odd.append(ele)
    # print(s_even)
    # print(s_odd)
    # print(s_sub)
    if k == 10:
        print(len(s_even))
        return len(s_even)
    else:
        sum_substring(k+1)

sum_substring(1)