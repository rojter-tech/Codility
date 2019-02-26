#NumberOfDiscIntersections
#Compute the number of intersections in a sequence of discs.
#Author: Daniel Reuter
#Github: https://github.com/rojter-tech

def solution(A):
    n = len(A)
    minimums = n*[0]
    maximums = n*[0]
    encaps = n*[0]
    countsingular = 0
    for i in range(n):
        thismax = i + A[i]
        if thismax < n-1:
            encaps[i] = thismax - i
        else:
            encaps[i] = n - 1 - i
        thismin = i - A[i]
        thismax = i + A[i]
        minimums[i] = thismin
        maximums[i] = thismax
        if A[i] == 0:
            countsingular += 1
    print(encaps)
    setlengthmaxmins = len(set(minimums) | set(maximums))
    commonmaxmins = 2*n - setlengthmaxmins

    return sum(encaps) + commonmaxmins - countsingular


A = [1,5,2,1,4,0]
#A = [1,1,1]
#A = []
print(solution(A))