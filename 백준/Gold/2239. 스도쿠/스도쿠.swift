/*
 백트래킹 !!
 같은 열에 숫자가 있는가, 같은 행에 숫자가 있는가, 3X3 보드에 숫자가 있는가
 같은 블럭 -> (x // 3, y // 3) 이 같으면 같은 블럭 !
 
 1부터 차례대로 대입하고,,쭉쭉 하고난 후 안되면 돌아가는 방식?
 
 0인 위치를 처음에 모두 저장해둬야할까? -> 0인 위치들만 돌 수 있도록?
 */

import Foundation

var sudoku = [[Int]]()
var blank = [(Int, Int)]()

for i in 0..<9 {
    let arr = Array(readLine()!).map { Int(String($0))! }
    for j in 0..<9 {
        if arr[j] == 0 {
            blank.append((i, j))
        }
    }
    sudoku.append(arr)
}

func check_block(_ num: Int, _ x: Int, _ y: Int) -> Bool {
    let dx = (x / 3) * 3, dy = (y / 3) * 3
    
    for i in 0..<3 {
        for j in 0..<3 {
            let nx = dx + i, ny = dy + j
            if nx != x && ny != y && sudoku[nx][ny] == num {
                return false
            }
        }
    }
    return true
}

func check_column(_ num: Int, _ x: Int, _ y: Int) -> Bool {
    for i in 0..<9 {
        if i != x && sudoku[i][y] == num {
            return false
        }
    }
    return true
}

func back(_ i: Int) {
    
    if i == blank.count {
        for x in 0..<9 {
            print(sudoku[x].map({String($0)}).joined(separator: ""))
        }
        exit(0)
    }
    
    let x = blank[i].0, y = blank[i].1
    for num in 1...9 {
        if !sudoku[x].contains(num) && check_block(num, x, y) && check_column(num, x, y) {
            sudoku[x][y] = num
            back(i + 1)
            sudoku[x][y] = 0
        }
    }
}

back(0)
