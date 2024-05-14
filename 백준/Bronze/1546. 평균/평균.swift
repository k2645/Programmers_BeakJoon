let N = Int(readLine()!)!
var scores = readLine()!.split(separator: " ").map { Double($0)! }
let max_score = scores.max()!

let score_sum = scores.reduce(0) { $0 + ($1 / max_score * 100) }
print(score_sum / Double(N))
