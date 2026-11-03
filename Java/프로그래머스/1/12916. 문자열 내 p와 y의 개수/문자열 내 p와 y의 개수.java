import java.util.Arrays;

class Solution {
    boolean solution(String s) {
        String[] arr = s
            .toLowerCase()
            .split("");
        
        int p = 0;
        int y = 0;
        
        for (int i = 0; i < arr.length; i++) {
            if (arr[i].equals("p")) {
                p += 1;
            } else if (arr[i].equals("y")) {
                y += 1;
            }
        }

        return p == y;
    }
}