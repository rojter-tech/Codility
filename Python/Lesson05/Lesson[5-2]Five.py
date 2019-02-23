#Author: Daniel Reuter
#Github: https://github.com/rojter-tech

def letter_presums(A):
    n = len(A)
    ASums = (n + 1)*[0];    CSums = (n + 1)*[0]
    GSums = (n + 1)*[0];    TSums = (n + 1)*[0]
    for k in range(0,n):
        if A[k] == "A":
            ASums[k + 1] = ASums[k] + 1
        else:
            ASums[k + 1] = ASums[k]
        if A[k] == "C":
            CSums[k + 1] = CSums[k] + 1
        else:
            CSums[k + 1] = CSums[k]
        if A[k] == "G":
            GSums[k + 1] = GSums[k] + 1
        else:
            GSums[k + 1] = GSums[k]
        if A[k] == "T":
            TSums[k + 1] = TSums[k] + 1
        else:
            TSums[k + 1] = TSums[k]
        
    return ASums, CSums, GSums, TSums

def slice_minimal(p, q, ASums, CSums, GSums, TSums):
    freq = ASums[q + 1] - ASums[p]
    if freq > 0:
        return 1
    freq = CSums[q + 1] - CSums[p]
    if freq > 0:
        return 2
    freq = GSums[q + 1] - GSums[p]
    if freq > 0:
        return 3
    freq = TSums[q + 1] - TSums[p]
    if freq > 0:
        return 4

def solution(S, P, Q):
    ASums, CSums, GSums, TSums = letter_presums(S)
    minimpactList = []
    for p, q in zip(P,Q):
        thismin = slice_minimal(p, q, ASums, CSums, GSums, TSums)
        minimpactList.append(thismin)
    
    return minimpactList

S = "CAGCCTA"   ;  P = [2,5,0];    Q = [4,5,6]
#S = "T"        ;  P = [0];        Q = [0]

print(solution(S,P,Q))