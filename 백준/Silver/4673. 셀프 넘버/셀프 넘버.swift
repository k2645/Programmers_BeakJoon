import Foundation

var arr = Set<Int>(1...10000)
var generate_num = Set<Int>()
var idx = 0

for i in 1...10000 {
    var num = i
    for j in String(num) {
        num += Int(String(j))!
    }
    generate_num.insert(num)
}

for num in Array(arr.subtracting(generate_num)).sorted() {
    print(num)
}
