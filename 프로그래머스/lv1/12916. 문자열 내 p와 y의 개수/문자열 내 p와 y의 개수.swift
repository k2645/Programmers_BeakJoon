import Foundation

func solution(_ s:String) -> Bool
{
    var pNum: Int = 0
    var yNum: Int = 0
    
    for char in s {
        if char == "p" || char == "P" { pNum += 1}
        if char == "y" || char == "Y" { yNum += 1}
    }
    
    if pNum == yNum { return true }
    else { return false }

}
