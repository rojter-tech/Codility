def quicksort(A):
    n = len(A)
    if n == 0: return []
    pivot = A[-1]
    leftA = []
    rightA = []
    for i in range(n - 1):
        if A[i] >= pivot:
            rightA.append(A[i])
        else:
            leftA.append(A[i])
    concat = quicksort(leftA) + [pivot] + quicksort(rightA)
    return concat

def solution(A):
    sortedA = quicksort(A)
    trackelem = 10**6 + 1
    uniqueelem = 0
    for elem in sortedA:
        if elem != trackelem:
            trackelem = elem
            uniqueelem = uniqueelem + 1

    return uniqueelem


A = [1,1,1,2,3,3]
print(solution(A))