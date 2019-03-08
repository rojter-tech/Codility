import java.util.*;
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

class Solution {
    public static int solution(int[] A) {
        int n = A.length;
        int[][] edgepoints = new int[2*n][2];
        //List<int[]> edgepoints = new ArrayList<>();
        int[] alter = {-1,1};
        for (int i = 0; i < 2*n; i++) {
            if (A[i/2] > 2147483646) {A[i/2] = 2147483646;}
            int edgetype = alter[i%2];
            int[] thisedge = {i/2 - A[i/2]*edgetype, edgetype};
            //edgepoints.add(thisedge);
            edgepoints[i] = thisedge;
        }
        
        Arrays.sort(edgepoints, new Comparator<int[]>() {
            @Override
            public int compare(int[] o1, int[] o2) {
                return Integer.compare(o2[1], o1[1]);
            }
        });

        Arrays.sort(edgepoints, new Comparator<int[]>() {
            @Override
            public int compare(int[] o1, int[] o2) {
                return Integer.compare(o1[0], o2[0]);
            }
        });

        for (int[] edge : edgepoints) {
            System.out.println(Arrays.toString(edge));
        }

        int edgesum = 0;
        int intersectsum = 0;
        for (int[] edge : edgepoints) {
            edgesum = edgesum + edge[1];
            if (edge[1] == -1) {
                intersectsum = intersectsum + edgesum;
            }
            if (intersectsum > (int) 1E7) {
                return -1;
            }
        }
        return intersectsum;
    }
}

/**
 * LessonSixFour
 */
public class LessonSixFour {

    public static void main(String[] args) {
        //int[] A = {1,1,1};
        int[] A = {1, 5, 2, 1, 4, 0};
        //int [] A = {1, 2147483647, 0};
        System.out.println(Solution.solution(A));
    }
}
