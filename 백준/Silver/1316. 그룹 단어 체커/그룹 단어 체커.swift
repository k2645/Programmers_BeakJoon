import Foundation

let N = Int(readLine()!)!
var cnt: Int = 0

for _ in 0..<N {
    let string = Array(readLine()!)
    var string_char = Set<String>()
    var isGroup = true
    for (idx, char) in string.enumerated() {
        if idx > 0 && string[idx - 1] != char {
            if string_char.contains(String(char)) {
                isGroup = false
                break
            }
        }
        string_char.insert(String(char))
    }
    if isGroup { cnt += 1 }
}

print(cnt)
