import Foundation

func solution(_ n:Int) -> [Int] {
    
    var arr = Array<Int>(1...n).filter { $0 % 2 == 1 }
    
    return arr
    
}
