import Foundation

func solution(_ price:Int) -> Int {
    
    var payment: Double = 0
    
    switch price {
    case 0..<100000:
        payment = Double(price)
    case 100000..<300000:
        payment = Double(price) * 0.95
    case 300000..<500000:
        payment = Double(price) * 0.90
    default:
        payment = Double(price) * 0.80
    }
    
    return Int(payment)
}