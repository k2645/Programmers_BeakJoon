import Foundation

func solution(_ name:String) -> Int {
    
    var name_arr = Array(name)
    var updown: Int = 0
    var leftright: Int = name.count - 1
    let aValue = Int(Character("A").asciiValue!)
    let zValue = Int(Character("Z").asciiValue!)
    
    for nowIdx in 0..<name.count {
        // 알파벳 맞추는 controll 카운트
        if let value = name_arr[nowIdx].asciiValue {
            if Int(value) - aValue <= 13 {
                updown += Int(value) - aValue
            } else {
                updown += zValue - Int(value) + 1
            }
        }
        
        // 현재 인덱스의 뒷부분에서 "A"의 길이가 가장 긴 부분의 마지막 인덱스값 구하기
        var endIdx = nowIdx + 1
        while endIdx < name.count && name_arr[endIdx] == "A" {
            endIdx += 1
        }
        
        // 1. "A"의 길이가 가장 긴 부분을 기준으로 앞으로 갔다가 뒤로 이동하는 경우
        let moveFront = nowIdx * 2 + (name_arr.count - endIdx)
        // 2. "A"의 길이가 가장 긴 부분을 기준으로 뒤로 갔다가 앞으로 이동하는 경우
        let moveBack = nowIdx + (name_arr.count - endIdx) * 2
        
        leftright = min(leftright, moveFront)
        leftright = min(leftright, moveBack)
    }
    
    return updown + leftright
}
