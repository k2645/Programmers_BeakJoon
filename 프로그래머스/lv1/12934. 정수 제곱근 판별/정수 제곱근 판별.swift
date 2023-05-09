import Foundation

func solution(_ n:Int64) -> Int64 {
    
    var x = Int64(sqrt(Double(n)))
    
    return x * x == n ? ((x + 1)*(x + 1)) : -1
}
