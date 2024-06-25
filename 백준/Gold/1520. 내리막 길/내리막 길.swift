/*
 DFS / DP 사용
 dp를 어떻게 사용할 수 있을까...?
 
 */

import Foundation

let mn = readLine()!.split(separator: " ").map { Int($0)! } // 순서대로 M, N
let M = mn[0]
let N = mn[1]
var board = [[Int]]()
var dp = [[Int]](repeating: [Int](repeating: -1, count: N), count: M)

for _ in 0..<M {
    let arr = readLine()!.split(separator: " ").map { Int($0)! }
    board.append(arr)
}

func dfs(_ x: Int, _ y: Int) -> Int {
    dp[x][y] = 0
    if x == M - 1 && y == N - 1 {
        dp[x][y] = 1
        return dp[x][y]
    }
    let directions = [(-1, 0), (0, -1), (0, 1), (1, 0)]
    for (dx, dy) in directions {
        let nx = x + dx, ny = y + dy
        if 0 <= nx && nx < M && 0 <= ny && ny < N && board[nx][ny] < board[x][y] {
            if dp[nx][ny] == -1 {
                dp[nx][ny] = dfs(nx, ny)
            }
            dp[x][y] += dp[nx][ny]
        }
    }
    return dp[x][y]
}

print(dfs(0, 0))
