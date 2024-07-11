/*
기울기: h/w가 자연수가 되게 하는 값.

0...n까지 n은 h/w가 자연수가 되게 하는 값.
1단위로 끊어가며 몇개의 블럭씩 제거해야하는지 count

*/

import Foundation

func gcd(_ a: Int, _ b: Int) -> Int {
    if b == 0 {
        return a
    } else {
        return gcd(b, a % b)
    }
}

func solution(_ w: Int, _ h: Int) -> Int64 {

    let gcdNum = gcd(min(w, h), max(w, h)) // 최대공약수
    let minW = min(w/gcdNum, h/gcdNum)
    let minH = max(w/gcdNum, h/gcdNum)
    let tilt = Double(minH) / Double(minW)
    var count: Int64 = 0
    for i in 0..<minW {
        count += Int64(ceil(Double(minH * (i + 1)) / Double(minW)) - floor(Double(minH * i) / Double(minW)))
    }
    
    return Int64(w * h) - (count * Int64(gcdNum))
}