def solution(A):
    A.sort()
    iterator = 0
    for elem in A:
        iterator = iterator + 1
        if elem != iterator:
            return 0
    return 1

A = [3,1,2]
print(solution(A))