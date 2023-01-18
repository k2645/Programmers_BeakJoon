import Foundation

func solution(_ array:[Int]) -> Int {
    
    let removedDuplicate: Array = Array(Set(array))
    var dic: Dictionary = [Int:Int]()
    
    for arr in removedDuplicate {
        dic[arr] = array.filter{ ($0) == arr }.count
    }
    
    let maxCount = dic.values.max()
    var count: Int = 0
    
    for (_, value) in dic {
        if maxCount == value { count += 1 }
    }
    
    if count > 1 {
        return -1
    } else {
        for (key, value) in dic {
            if value == maxCount { return key }
        }
    }
    
    return -1
}