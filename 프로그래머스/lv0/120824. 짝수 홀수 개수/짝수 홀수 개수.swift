import Foundation

func solution(_ num_list:[Int]) -> [Int] {
    
    var even_odd: [Int] = [0, 0]
    
    for num in num_list {
        if num % 2 == 0 {
            even_odd[0] += 1
        } else {
            even_odd[1] += 1
        }
    }
    
    return even_odd
}