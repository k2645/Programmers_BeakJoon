import Foundation

func solution(_ absolutes:[Int], _ signs:[Bool]) -> Int {
    
    var result: Int = 0
    
    for (idx, num) in absolutes.enumerated() {
        if signs[idx] {
            result += num
        } else {
            result -= num
        }
    }
    
    return result
}
