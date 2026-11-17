import java.util.*;

class Solution {
    public String solution(int n, int t, int m, int p) {
        
        String fullRadix = "";
        for(int i = 0; fullRadix.length() < t * m; i++) {
            fullRadix += Integer.toString(i, n);
        }
        
        String answer = "";
        p -= 1;
        for(int i = 0; i < t; i++) {
            answer += String.valueOf(fullRadix.charAt(i * m + p));
        }
        
        return answer.toUpperCase();
    }
}