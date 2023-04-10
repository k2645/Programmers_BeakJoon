import Foundation

func solution(_ bridge_length:Int, _ weight:Int, _ truck_weights:[Int]) -> Int {
    
    var bridgeArray = [Int](repeating: 0, count: bridge_length)
    var bridgeWeight: Int = 0
    var totalSec: Int = 0
    var trucks = truck_weights.reversed() as [Int]
    
    while !trucks.isEmpty {
        totalSec += 1
        bridgeWeight -= bridgeArray.remove(at: 0)
        if bridgeWeight + trucks.last! <= weight {
            bridgeWeight += trucks.last!
            bridgeArray.append(trucks.popLast()!)
        } else {
            bridgeArray.append(0)
        }
    }
    totalSec += bridge_length
    
    return totalSec
}