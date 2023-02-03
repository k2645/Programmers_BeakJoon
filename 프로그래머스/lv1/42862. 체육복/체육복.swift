import Foundation

func solution(_ n:Int, _ lost:[Int], _ reserve:[Int]) -> Int {
    
    var lost_arr = lost
    var reserve_arr = reserve
    var count: Int = 0
    
    for num in lost_arr {
        if reserve_arr.contains(num), let idx1 = lost_arr.firstIndex(of: num), let idx2 = reserve_arr.firstIndex(of: num) {
            lost_arr.remove(at: idx1)
            reserve_arr.remove(at: idx2)
        }
    }
    
    for num in 1...n {
        if lost_arr.contains(num) {
            if reserve_arr.contains(num - 1) {
                if let index = reserve_arr.firstIndex(of: num - 1) {
                    reserve_arr.remove(at: index)
                    count += 1
                }
            } else if reserve_arr.contains(num + 1) {
                if let index = reserve_arr.firstIndex(of: num + 1) {
                    reserve_arr.remove(at: index)
                    count += 1
                }
            }
        } else {
            count += 1
        }
    }
    
    
    return count
}
