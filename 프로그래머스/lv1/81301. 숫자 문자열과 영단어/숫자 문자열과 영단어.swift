import Foundation

func solution(_ s:String) -> Int {
    
    let words = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    var result = s
    
    for (index, word) in words.enumerated() {
        result = result.replacingOccurrences(of: word, with: String(index))
    }
    
    return Int(result)!
}