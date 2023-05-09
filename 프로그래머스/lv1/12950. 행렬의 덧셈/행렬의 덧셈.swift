func solution(_ arr1:[[Int]], _ arr2:[[Int]]) -> [[Int]] {
    
    var sumList: [[Int]] = []
    
    for (i, _) in arr1.enumerated() {
        var sumRow: [Int] = []
        for (j, _) in arr1[i].enumerated() {
            sumRow.append(arr1[i][j] + arr2[i][j])
        }
        sumList.append(sumRow)
    }
    
    return sumList
}
