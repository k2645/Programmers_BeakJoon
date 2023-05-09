func solution(_ arr:[Int], _ divisor:Int) -> [Int] {
    
    var result: [Int] = []
    
    for num in arr {
        if num % divisor == 0 {
            result.append(num)
        }
    }
    
    return result.isEmpty ? [-1] : result.sorted()
}
