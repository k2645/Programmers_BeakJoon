import Foundation

func solution(_ s: String) -> [Int] {
    
    let startIndex = s.index(s.startIndex, offsetBy: 1)
    let endIndex = s.index(s.endIndex, offsetBy: -1)
    var tuples = [[Int]]()
    for str in s[startIndex..<endIndex].components(separatedBy: ["{", "}"]) {
        let arr = str.split(separator: ",")
        if !arr.isEmpty {
            tuples.append(arr.map { Int($0)! })
        }
    }
    
    tuples.sort { $0.count < $1.count }
    
    var ans = [Int]()
    for tuple in tuples {
        let a = Set(ans)
        let t = Set(tuple)
        ans += Array(t.subtracting(a))
    }
    
    return ans
}