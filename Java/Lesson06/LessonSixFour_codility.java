import java.util.*;

class Solution {

 public static int solution(int[] A) {

        if (A.length < 2) {return 0;}

        Long r[] = new Long[A.length];
        Long l[] = new Long[A.length];

        for (int i = 0; i < A.length; i++) {
            if (A[i] == 0) {
                r[i] = l[i] = (long) i;
            } else {
                r[i] = (long) i + A[i];
                l[i] = (long) i - A[i];
            }
        }

        Arrays.sort(r);
        Arrays.sort(l);

        int in = 0;
        long s = 0;
        for (int i = 0; i < l.length; i++) {
            if (l[i] > r[in]) {
                int y = 0;
                while (in < r.length && l[i] > r[in]) {
                    y++;
                    in++;
                }
                if (y > 0) {
                    s = s + (l.length - i) * y;
                }
            }
        }

        long t = (((long) A.length) * ((long) A.length - 1)) / 2;
        if ((t - s) > 10000000)
            return -1;
        return (int) (t - s);
    
    }
}

    public class LessonSixFour_codility {

        public static void main(String[] args) {
            //int[] A = {1,1,1};
            int[] A = {1, 5, 2, 1, 4, 0};
            //int [] A = {1, 2147483647, 0};
            System.out.println(Solution.solution(A));
        }
    }