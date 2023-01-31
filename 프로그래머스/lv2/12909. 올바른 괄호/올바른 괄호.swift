import Foundation

func solution(_ s:String) -> Bool
{
    var ans:Bool = false
    
    var count: Int = 0
    
    if s[s.startIndex] == ")" { return ans }
    
    for i in s {
        if i == "(" {
            count += 1
        } else {
            count -= 1
        }
        if count < 0 {
            return false
        }
    }

    return count == 0 ? true : false
}