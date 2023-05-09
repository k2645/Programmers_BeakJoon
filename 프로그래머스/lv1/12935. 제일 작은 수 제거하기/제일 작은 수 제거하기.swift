func solution(_ arr:[Int]) -> [Int] {
    
    var result = arr
    let minIdx = result.firstIndex(of: arr.min()!)!
    
    result.remove(at: minIdx)
    
    return result.isEmpty ? [-1] : result
}
