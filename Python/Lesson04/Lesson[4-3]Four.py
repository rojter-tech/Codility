#Author: Daniel Reuter
#Github: https://github.com/rojter-tech

def organizeset(A):
    setmax = max(A)
    upperlimit = 10**5

    if setmax >= upperlimit:
        sortedA = upperlimit*[0]
    else:
        sortedA = setmax*[0]
    
    N = len(A)
    countelem = 0
    for i in range(N):
        if A[i] > 0 and A[i] <= upperlimit:
            sortindex = A[i] - 1
            sortedA[sortindex] = A[i]
            countelem = countelem + 1
    
    if countelem == 0:
        return None
    else:
        return sortedA

def solution(A):
    sortedA = organizeset(A)
    if sortedA is None:
        return 1
    
    subseqcontrval = 0
    for elem in sortedA:
        if elem != 0:
            subseqcontrval = subseqcontrval + 1
        elif elem == 0:
            return subseqcontrval + 1
    
    return sortedA[-1] + 1

A0 = (-1)*list(range(1,10**6))
A1 = list(range(0,10**6))

A = A0 + A1 + [10**6]
A.remove(1012)

#A = [1, 3, 6, 4, 1, 2, 5]
print(solution(A))