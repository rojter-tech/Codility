#OddOccurrencesInArray
#Author: Daniel Reuter
#Github: https://github.com/rojter-tech

def solution(A):
    A.sort()
    arraylength = len(A)
    if arraylength == 1:
        return A[0]

    evenindex = []
    for i in range(arraylength):
        if i%2 == 0: 
            evenindex.append(i)
    evenindex.remove(evenindex[-1])

    for i in evenindex:
        if A[i] != A[i + 1]:
            return A[i]

    return A[arraylength - 1]

A = [1,1,2,2,3]
B = solution(A)
print(B)