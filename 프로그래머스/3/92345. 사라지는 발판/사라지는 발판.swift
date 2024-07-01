import Foundation

func solution(_ board:[[Int]], _ aloc:[Int], _ bloc:[Int]) -> Int {
    return solve(board, aloc[0], aloc[1], bloc[0], bloc[1]).1
}

func is_finished(_ board: [[Int]], _ x: Int, _ y: Int) -> Bool {
    let dir = [(-1, 0), (0, -1), (1, 0), (0, 1)]
    let h = board.count
    let w = board[0].count
    for i in 0..<4 {
        let nx = x + dir[i].0
        let ny = y + dir[i].1
        if 0 <= nx && nx < h && 0 <= ny && ny < w && board[nx][ny] == 1 {
            return false
        }
    }
    return true
}

func solve(_ board:[[Int]], _ x1: Int, _ y1: Int, _ x2: Int, _ y2: Int) -> (Bool, Int) {

    if is_finished(board, x1, y1) { return (false, 0) }
    
    if x1 == x2 && y1 == y2 { return (true, 1) }
    
    var min_turn = 987654321
    var max_turn = 0
    var can_win = false
    var board = board
    
    let dir = [(-1, 0), (0, -1), (1, 0), (0, 1)]
    let h = board.count
    let w = board[0].count
    for i in 0..<4 {
        let nx = x1 + dir[i].0
        let ny = y1 + dir[i].1
        if 0 > nx || nx >= h || 0 > ny || ny >= w || board[nx][ny] == 0 { continue }
        
        board[x1][y1] = 0
        let result = solve(board, x2, y2, nx, ny)
        board[x2][y2] = 1
        
        if !result.0 {
            can_win = true
            min_turn = min(min_turn, result.1)
        } else if !can_win {
            max_turn = max(max_turn, result.1)
        }
    }
    
    let turn = can_win ? min_turn : max_turn
    
    return (can_win, turn + 1)
}