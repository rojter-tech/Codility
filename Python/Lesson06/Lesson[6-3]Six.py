#Triangle
#Determine whether a triangle can be built from a given set of edges.
#Author: Daniel Reuter
#Github: https://github.com/rojter-tech

def solution(A):
    n = len(A)
    sortedA = sorted(A)
    for i in range(n-2):
        cond_one    = (sortedA[i]   + sortedA[i+1] > sortedA[i+2])
        cond_two    = (sortedA[i+1] + sortedA[i+2] > sortedA[i]  )
        cond_three  = (sortedA[i+2] + sortedA[i]   > sortedA[i+1])
        isTriangular = cond_one and cond_two and cond_three
        if isTriangular:
            return 1
    return 0

N = 50000
A1 = N*[-2]
A2 = N*[1]
A = [10,2,5,1,8,20]
print(solution(A))