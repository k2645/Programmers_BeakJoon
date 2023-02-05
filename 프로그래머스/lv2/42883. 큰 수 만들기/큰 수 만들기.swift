import Foundation

func solution(_ number:String, _ k:Int) -> String {
    
    var result = ""
    var num_arr = number.map { Int(String($0))! }
    var num_stack: [Int] = []
    var delete_cnt = 0
    var idx = 0
    
    while delete_cnt < k && idx < num_arr.count {
        
        guard let last = num_stack.last else {
            num_stack.append(num_arr[idx])
            idx += 1
            continue
        }
        
        if last < num_arr[idx] {
            num_stack.removeLast()
            delete_cnt += 1
        } else {
            num_stack.append(num_arr[idx])
            idx += 1
        }
        
    }
    
    if num_stack.count < number.count - k {
        num_stack.append(contentsOf: num_arr[idx...])
    }
    
    if delete_cnt < k {
        num_stack.removeLast(k - delete_cnt)
    }
    
    result = num_stack.map { String($0) }.joined()
    
    return result
}