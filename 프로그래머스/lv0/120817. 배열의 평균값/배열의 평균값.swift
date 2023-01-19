import Foundation

func solution(_ numbers:[Int]) -> Double {
    
    let sum: Double = Double(numbers.reduce(0) { $0 + $1 })
    
    return sum / Double(numbers.count)
}