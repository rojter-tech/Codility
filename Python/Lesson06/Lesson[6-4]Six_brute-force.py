#NumberOfDiscIntersections
#Compute the number of intersections in a sequence of discs.
#Author: Daniel Reuter
#Github: https://github.com/rojter-tech

#Brute-Force
def solution(A):
    n = len(A)
    setA = set([])
    discSet = n*[None]
    intersectSet = []
    totalintersects = 0
    for i in range(n):
        minval = i - A[i]
        maxval = i + A[i]
        thisset = list(range(minval,maxval+1))
        discSet[i] = set(thisset)
        setA = setA | discSet[i]
    for disc in discSet:
        thisintersect = set(list(disc & setA))
        intersectSet.append(thisintersect)
    for i in range(n):
        numberofintersects = 0
        for j in range(i,n-1):
            intersectlength = len(intersectSet[i] & intersectSet[j+1])
            if intersectlength > 0:
                numberofintersects += 1
        totalintersects += numberofintersects
    return totalintersects


maxint = 2147483647
maxintersections = 10000000
A = [1, 2147483647, 0]
#A = [5,4,2,1,1,0]
print(solution(A))