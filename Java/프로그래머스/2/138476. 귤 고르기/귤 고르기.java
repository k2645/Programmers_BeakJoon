import java.util.HashMap;
import java.util.Map;
import java.util.Arrays;
import java.util.Collections;

class Solution {
    public int solution(int k, int[] tangerine) {
        Map<Integer, Integer> dict = new HashMap<>();
        
        for(int i = 0; i < tangerine.length; i++) {
            if (dict.containsKey(tangerine[i])) {
                dict.put(tangerine[i], dict.get(tangerine[i]) + 1);
            } else {
                dict.put(tangerine[i], 1);
            }
        }
        
        Integer[] arr = dict.values().toArray(new Integer[0]);
        Arrays.sort(arr, Collections.reverseOrder());
        
        int answer = 0;
        int sum = 0;
        for(int i = 0; sum < k; i++) {
            sum += arr[i];
            answer += 1;
        }
        return answer;
    }
}