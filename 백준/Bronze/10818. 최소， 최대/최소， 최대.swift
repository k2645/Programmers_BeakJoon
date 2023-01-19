import Foundation

let _ = readLine()
let array : [Int] = readLine()!.split(separator: " ").map { Int(String($0))! }
print(array.min()!, array.max()!)

/* 
components를 사용하면 "시간초과" → .split 사용
min(), max()의 시간복잡도는 O(n)
Substring → Int 로 바로 변형하는 것 보다, Substring → String → Int 로 변환하는 것이 더 빠르다.
*/