import Foundation

func solution(_ n:Int) -> Int { // 최소공배수
    
    var result: Int = 0
    
    if n > 6 {
        result = (n * 6 / gcd(n, 6)) / 6
    } else {
        result = (n * 6 / gcd(6, n)) / 6
    }
    
    return result
}

func gcd(_ a: Int, _ b: Int) -> Int {
    if b == 0 { 
        return  a 
    } else {
        return gcd(b, a % b)
    }
}