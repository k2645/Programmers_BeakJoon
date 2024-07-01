import Foundation

let N = Int(readLine()!)!
let health = readLine()!.split(separator: " ").map { Int($0)! }
let joy = readLine()!.split(separator: " ").map { Int($0)! }
var dp = [[Int]](repeating: [Int](repeating: 0, count: 100), count: N + 1) // 100이 되면 어차피 0이니까..

for i in 0...N {
    for j in 0..<100 {
        if i == 0 || j == 0 {
            dp[i][j] = 0
        } else if health[i - 1] <= j {
            dp[i][j] = max(joy[i - 1] + dp[i - 1][j - health[i - 1]], dp[i - 1][j])
        } else {
            dp[i][j] = dp[i - 1][j]
        }
    }
}

print(dp[N][99])
