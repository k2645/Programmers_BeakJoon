import Foundation

func solution(_ a:[Int], _ b:[Int]) -> Int {
    
    var dotProduct: Int = 0
    
    for idx in 0..<a.count {
        dotProduct += (a[idx] * b[idx])
    }
    
    return dotProduct
}
