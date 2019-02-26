#NumberOfDiscIntersections
#Compute the number of intersections in a sequence of discs.
#Author: Daniel Reuter
#Github: https://github.com/rojter-tech

#Brute-Force
def solution(A):
    n = len(A)
    centermindict = {}
    for i in range(n):
        centermindict[i] = i - A[i]
    centermintuple = sorted(centermindict.items(), key=lambda x: x[1])

    nextmins = n*[0]
    intersectsum = 0
    for i in range(n):
        j = 0
        end = n - i
        thismax = i + abs(i - centermindict[i])
        nextmin = centermintuple[j][1]
        while nextmin <= thismax and j < end:
            j += 1
            if j < end:
                nextmin = centermintuple[j][1]
            nextmins[i] += 1
        nextmins[i] -= 1
        centermintuple.remove((i,centermindict[i]))
        intersectsum += nextmins[i]
        if intersectsum > 10000000:
            return -1
    

    return intersectsum

A = [1,5,2,1,4,0]
print(solution(A))
print()