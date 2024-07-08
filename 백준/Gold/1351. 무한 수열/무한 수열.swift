import Foundation

let arr = readLine()!.split(separator: " ").map { Int($0)! }
let N = arr[0], P = arr[1], Q = arr[2]
var dp = [Int: Int]()
dp[0] = 1
dp[1] = 2

func recursion(_ n: Int) -> Int {
    if let num = dp[n] { return num }
    
    if n/P == n/Q {
        dp[n] = recursion(n/P) * 2
    } else {
        dp[n] = recursion(n/P) + recursion(n/Q)
    }
    return dp[n]!
}

print(recursion(N))