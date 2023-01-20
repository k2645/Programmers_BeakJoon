import Foundation

let n = readLine()!.components(separatedBy: [" "]).map { Int($0)! }

for i in 1...n.first! {
    print(String(repeating: "*", count: i))
}
