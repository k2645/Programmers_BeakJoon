class Solution {
    public int solution(String[] babbling) {
        int answer = 0;
        String[] able = {"aya", "ye", "woo", "ma"};
        
        for(int i = 0; i < babbling.length; i++) {
            String bab = babbling[i];
            String prev = "";
            while (bab.length() > 0) {
                boolean flag = false;
                for(int j = 0; j < 4; j++) {
                    if (bab.startsWith(able[j]) && !prev.equals(able[j])) {
                        prev = able[j];
                        bab = bab.substring(able[j].length());
                        flag = true;
                        break;
                    }
                }
                if (!flag) { break; }
            }
            
            if (bab.length() == 0) { answer += 1; }
        }
        return answer;
    }
}