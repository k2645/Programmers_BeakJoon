func solution(_ arr:[Int]) -> Double {
    
    let arrSum: Double = Double(arr.reduce(0, +))
    let arrCnt: Double = Double(arr.count)
    
    return arrSum / arrCnt
}
