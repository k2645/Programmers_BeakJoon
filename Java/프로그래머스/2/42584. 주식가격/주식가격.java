import java.util.*;

record Pair<A, B>(A idx, B price) {}

class Solution {
    public int[] solution(int[] prices) {
        int[] answer = new int[prices.length];
        
        Deque<Pair<Integer, Integer>> stack = new ArrayDeque<>();
        stack.push(new Pair<>(0, prices[0]));
            
        for(int i = 1; i < prices.length; i++) {
            while (!stack.isEmpty() && prices[i] < stack.peek().price()) {
                Pair<Integer, Integer> popped = stack.pop();
                answer[popped.idx()] = i - popped.idx();
            }
            stack.push(new Pair<>(i, prices[i]));
        }
        
        int lastIdx = stack.pop().idx();
        while(!stack.isEmpty()) {
            Pair<Integer, Integer> popped = stack.pop();
            answer[popped.idx()] = lastIdx - popped.idx();
        }
        
        return answer;
    }
}