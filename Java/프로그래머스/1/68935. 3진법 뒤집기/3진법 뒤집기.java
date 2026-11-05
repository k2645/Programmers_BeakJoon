class Solution {
    public int solution(int n) {
        String base3 = Integer.toString(n, 3);
        String reverseBase3 = "";
        
        for(int i = base3.length() - 1; i >= 0 ; i--) {
            reverseBase3 += base3.charAt(i);
        }
        
        return Integer.parseInt(reverseBase3, 3);
    }
}