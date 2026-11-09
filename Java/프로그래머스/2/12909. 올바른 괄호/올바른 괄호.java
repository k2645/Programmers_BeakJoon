import java.util.ArrayDeque;
import java.util.Deque;

class Solution {
    boolean solution(String s) {
        Deque<String> stack = new ArrayDeque<>();
        
        if (s.length() % 2 == 1) { return false; }
        
        for(int i = 0; i < s.length(); i++) {
            switch (String.valueOf(s.charAt(i))) {
                case "(":
                    stack.push("(");
                    break;
                case ")":
                    if (!stack.isEmpty() && stack.peek().equals("(")) {
                        stack.pop();
                    } else {
                        stack.push(")");
                    }
            }
        }

        return stack.isEmpty();
    }
}