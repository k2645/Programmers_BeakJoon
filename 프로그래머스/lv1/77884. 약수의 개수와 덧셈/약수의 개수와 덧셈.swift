import Foundation

func solution(_ left:Int, _ right:Int) -> Int {
    
    var result: Int = 0
    
    for i in left...right {
        var measureNum = 0
        
        for k in 1...i {
            if i % k == 0 { measureNum += 1 }
        }
        
        if measureNum % 2 == 0 { result += i }
        else { result -= i }
        
    }
    
    return result
}
