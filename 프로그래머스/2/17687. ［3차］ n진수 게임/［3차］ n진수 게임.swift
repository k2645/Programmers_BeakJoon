/*
진법 변환...이새끼는 맨날나오는데 맨날 헷갈려 미친넘
2진수 -> 10진수는 Int(value, radix: 2)!
10진수 -> 2진수는 String(value, radix: 2)
2진수 -> 10진수 -> 16진수 String(value, radix: 16)

m * t개 문자들 중 p*i(i:0...t)번째 t개.
*/

func solution(_ n:Int, _ t:Int, _ m:Int, _ p:Int) -> String {
    
    var arr = [String]()
    var num = 0
    while arr.count <= m * t {
        arr += String(num, radix: n).map { String($0).uppercased() }
        num += 1
    }
    var result = [String]()
    for i in 0..<t {
        result.append(arr[(m * i) + (p - 1)])
    }
    
    return result.joined(separator:"")
}