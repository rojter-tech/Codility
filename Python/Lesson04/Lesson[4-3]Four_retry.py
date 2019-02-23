#Author: Daniel Reuter
#Github: https://github.com/rojter-tech

def keepallowedrange(A):
    Atmp = []
    countelem = 0
    for elem in A:
        if elem > 0 and elem <= 100000:
            Atmp.append(elem)
            countelem = countelem + 1
    if countelem == 0:
        return "null"
    else:
        return Atmp

def solution(A):
    reducedA = keepallowedrange(A)
    if reducedA == "null":
        return 1
    
    A_set = set(reducedA)
    subseqcontrval = 1
    for elem in A_set:
        if elem == 0:
            subseqcontrval = subseqcontrval - 1
        if elem != subseqcontrval:
            return subseqcontrval
        else:
            subseqcontrval = subseqcontrval + 1
    
    return max(reducedA) + 1

A0 = (-1)*list(range(1,1000000))
A1 = list(range(0,1000000))

A = [-1,-2,-3]
print(solution(A))