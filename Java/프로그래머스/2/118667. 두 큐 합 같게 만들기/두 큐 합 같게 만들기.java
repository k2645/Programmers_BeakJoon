import java.util.*;

class Solution {
    public int solution(int[] array1, int[] array2) {        
        Queue<Integer> queue1 = new ArrayDeque<>();
        Queue<Integer> queue2 = new ArrayDeque<>();
        long sum1 = 0;
        long sum2 = 0;
        
        for (int i = 0; i < array1.length; i++) { 
            queue1.add(array1[i]);
            queue2.add(array2[i]);
            sum1 += array1[i];
            sum2 += array2[i];
        }
        
        if ((sum1 + sum2) % 2 != 0) { return -1; }
        
        int cnt = 0;
        
        while (sum1 != sum2) {
            if (queue1.isEmpty() || queue2.isEmpty() || cnt >= array1.length * 3) { return -1; }
            
            if (sum1 < sum2) {
                Integer n = queue2.remove();
                sum2 -= n;
                queue1.add(n);
                sum1 += n;
            } else {
                Integer n = queue1.remove();
                sum1 -= n;
                queue2.add(n);
                sum2 += n;
            }
            cnt += 1;
        }
        
        return cnt;
    }
}