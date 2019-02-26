#NumberOfDiscIntersections
#Compute the number of intersections in a sequence of discs.
#Author: Daniel Reuter
#Github: https://github.com/rojter-tech

#Relative intersect at every point
def solution(A):
    n = len(A)
    if n < 2:
        return 0
    edgepoints = 2*n*[[0,0]]

    for i in range(2*n):
        edgepoints[i] = [int(i/2) - A[int(i/2)]*(-1)**i, (-1)**i]
    edgepoints.sort()
    edgepoints.append([0,0])
    
    edgesums = 0
    thisedgesum = 0
    j = 0
    while j < 2*n:
        thispoint = edgepoints[j][0]
        nextpoint = thispoint
        while nextpoint == thispoint and j < 2*n + 1:
            thisedgesum += edgepoints[j][1]
            j += 1
            nextpoint = edgepoints[j][0]
        
        if (j < 2*n) and thisedgesum - 1 > 0:
            edgesums += thisedgesum - 1
    return edgesums


if __name__ == '__main__':
    print('Testing solutions..')
    assert solution([1, 5, 2, 1, 4, 0]) == 11
    assert solution([]) == 0
    assert solution([0,1]) == 1
    assert solution([0, 0]) == 0
    assert solution([1,0,0,3]) == 4
    print('Test passed!')