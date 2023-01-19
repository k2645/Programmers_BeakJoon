import Foundation

func solution(_ num_list:[Int]) -> [Int] {
    
    var descending_list: [Int] = []
    
    for (index, _) in num_list.enumerated() {
        descending_list.append(num_list[num_list.count - index - 1])
    }
    
    return descending_list
}