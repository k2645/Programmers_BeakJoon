import Foundation

func solve(_ N: Int, _ priceArr: [Int], _ maxPrice: Int) -> [Int] {
    let index = priceArr.firstIndex(of: priceArr[1...].min()!)!
    
    if priceArr[index] > maxPrice { return [0] }
    
    let minIndex = priceArr.firstIndex(of: priceArr.min()!)!
    var result = [index]
    var resultSum = priceArr[index]
    while resultSum + priceArr[minIndex] <= maxPrice {
        result.append(minIndex)
        resultSum += priceArr[minIndex]
    }
    
    var remainPrice = maxPrice - resultSum
    for i in 0..<result.count {
        for n in stride(from: N - 1, through: 0, by: -1) {
            if remainPrice >= priceArr[n] - priceArr[result[i]] {
                remainPrice += priceArr[result[i]] - priceArr[n]
                result[i] = n
                break
            }
        }
    }
    
    return result
}

let N = Int(readLine()!)!
let priceArr = readLine()!.split(separator: " ").map { Int($0)! }
let maxPrice = Int(readLine()!)!

if N == 1 { print("0") }
else {
    print(solve(N, priceArr, maxPrice).map { String($0) }.joined())
}
