def solution(s):
    
    nums = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    
    for idx, num in enumerate(nums):
        s = s.replace(num, str(idx))
        
    return int(s)