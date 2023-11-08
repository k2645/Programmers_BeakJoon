func solution(_ arr:[Int]) -> Double {
    
    var avg: Double = 0
    
    avg = Double(arr.reduce(0, +)) / Double(arr.count)
    
    return avg
}