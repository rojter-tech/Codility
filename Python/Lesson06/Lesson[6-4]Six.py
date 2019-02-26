#NumberOfDiscIntersections
#Compute the number of intersections in a sequence of discs.
#Author: Daniel Reuter
#Github: https://github.com/rojter-tech

def solution(A):
    n = len(A)
    edgepoints, edgesum, intersectsum = 2*n*[0], 0, 0

    for i in range(2*n):
        edgepoints[i] = [int(i/2) - A[int(i/2)]*(-1)**i, (-1)**i]
    edgepoints.sort(key=lambda x: (x[0], -x[1]))

    for edge in edgepoints:
        if edge[1] > 0: intersectsum += edgesum
        edgesum += edge[1]
        if intersectsum > 1E7: return -1

    return intersectsum


if __name__ == '__main__':
    print('Testing solutions..')
    assert solution([1, 5, 2, 1, 4, 0]) == 11
    assert solution([]) == 0
    assert solution([0,1]) == 1
    assert solution([0, 0]) == 0
    assert solution([1,0,0,3]) == 4
    print('Test passed!')