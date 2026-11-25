import java.util.*;

class Solution {
    public int[] solution(int n, String[] words) {
        
        int[] answer = new int[2];
        String[] prevWords = new String[words.length];
        prevWords[0] = words[0];
        
        for(int i = 1; i < words.length; i++) {
            String prev = words[i - 1];
            String now = words[i];
            
            if (isWrong(prev, now, prevWords)) {
                answer[0] = i % n + 1;
                answer[1] = i / n + 1;
                break;
            }
            prevWords[i] = now;
        }

        return answer;
    }
    
    public boolean isWrong(String prev, String now, String[] prevWords) {
        return prev.charAt(prev.length() - 1) != now.charAt(0) || Arrays.asList(prevWords).contains(now);
    }
}