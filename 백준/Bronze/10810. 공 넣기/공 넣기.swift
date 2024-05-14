let nm = readLine()!.split(separator: " ").map { Int($0)! }
var basket = [String](repeating: "0", count: nm[0])

for _ in 0..<nm[1] {
    let arr = readLine()!.split(separator: " ").map { Int($0)! }
    for i in (arr[0] - 1)..<arr[1] {
        basket[i] = String(arr[2])
    }
}

print(basket.joined(separator: " "))
