#NumberOfDiscIntersections
#Compute the number of intersections in a sequence of discs.
#Author: Daniel Reuter
#Github: https://github.com/rojter-tech

#Brute-Force
def solution(A):
    n = len(A)
    nextminimums = n*[0]
    for i in range(n):
        for j in range(i,n-1):
            thismax = i + A[i]
            nextmin = j + 1 - A[j+1]
            if thismax >= nextmin:
                nextminimums[i] += 1
    return sum(nextminimums)


A = [1,5,2,1,4,0]
print(solution(A))