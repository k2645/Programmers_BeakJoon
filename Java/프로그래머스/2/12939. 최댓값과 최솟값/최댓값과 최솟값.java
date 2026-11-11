class Solution {
    public String solution(String s) {
        String[] str = s.split(" ");
        int min = Integer.MAX_VALUE;
        int max = Integer.MIN_VALUE;
        
        for(int i = 0; i < str.length; i++) {
            int value = Integer.parseInt(str[i]);
            min = Math.min(min, value);
            max = Math.max(max, value);
        }
        
        String answer = min + " " + max;
        return answer;
    }
}