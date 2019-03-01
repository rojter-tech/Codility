/*def solution(A):
    n = len(A)
    edgepoints, edgesum, intersectsum = 2*n*[[0,0]], 0, 0

    for i in range(2*n):
        edgepoints[i] = [int(i/2) - A[int(i/2)]*(-1)**i, (-1)**i]
    edgepoints.sort(key=lambda λ: [λ[0], -λ[1]])

    for edge in edgepoints:
        edgesum += edge[1]
        if edge[1] == -1: intersectsum += edgesum
        if intersectsum > 1E7: return -1

    return intersectsum
*/

/**
 * Lesson[6-4]Six
 */
public class Lesson[6-4]Six {

    
}