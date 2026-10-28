import java.util.*;

public class Solution {
    public int solution(int n) {
        int num = n;
        int answer = 0;

        while (num > 0) {
            answer += num % 10;
            num = num / 10;
        }

        return answer;
    }
}