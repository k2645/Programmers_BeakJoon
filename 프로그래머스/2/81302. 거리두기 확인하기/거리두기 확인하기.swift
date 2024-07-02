/*
bfs로 다른 참가자와 거리 찾기
*/
import Foundation

func solution(_ places:[[String]]) -> [Int] {
    
    var ans = [Int]()
    var dist = [Int]()
    var visited = [[Bool]]()
    let dx = [-1, 0, 1, 0]
    let dy = [0, -1, 0, 1]
    
    func dfs(_ places:[[String]], _ x: Int, _ y: Int, _ distance: Int) {
    
        if distance != 0 && places[x][y] == "P" {
            dist.append(distance)
            return
        }

        for i in 0..<4 {
            let nx = x + dx[i]
            let ny = y + dy[i]
            if 0 <= nx && nx < 5 && 0 <= ny && ny < 5 && !visited[nx][ny] && places[nx][ny] != "X" {
                visited[nx][ny] = true
                dfs(places, nx, ny, distance + 1)
                visited[nx][ny] = false
            }
        }
    }
    
    for place in places {
        var p = [[String]]()
        var loc = [(Int, Int)]()
        for i in 0..<5 { // 참가자 위치 찾기 및 배열로 변환
            let arr = Array(place[i]).map { String($0) }
            p.append(arr)
            if arr.contains("P") {
                for j in 0..<5 {
                    if arr[j] == "P" {
                        loc.append((i, j))
                    }
                }
            }
        }
        if loc.count <= 1 { 
            ans.append(1)
            continue
        }
        var isValid = 1
        for l in loc {
            dist = []
            visited = [[Bool]](repeating: [Bool](repeating: false, count: 5), count: 5)
            visited[l.0][l.1] = true
            dfs(p, l.0, l.1, 0)
            if let min_dist = dist.min() {
                if min_dist <= 2 {
                    isValid = 0
                    break
                }
            }
        }
        ans.append(isValid)
    }
    
    return ans
}