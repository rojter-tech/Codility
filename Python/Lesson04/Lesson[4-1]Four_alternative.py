#Author: Daniel Reuter
#Github: https://github.com/rojter-tech

def checkpair(A):
    for i in range(len(A) - 1):
        if A[i] == A[i + 1]:
            return 0
    return 1

def solution(A):
    A.sort()
    topelement = len(A)
    if checkpair(A) == 0:
        return 0
    elif A[-1] == topelement and A[0] == 1:
        return 1
    else:
        return 0

A = [9, 5, 7, 3, 2, 7, 3, 1, 10, 8]
print(solution(A))