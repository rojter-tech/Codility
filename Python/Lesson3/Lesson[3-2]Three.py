def solution(A):
    if len(A) == 1:
        if A[0] == 1:
            return 2
        else:
            return 1
    elif len(A) == 0:
        return 1
    
    A.sort()
    iterator = 1
    for elem in A:
        if elem != iterator:
            return iterator
        iterator = iterator + 1
    return A[-1] + 1

A = [1,2]
print(solution(A))