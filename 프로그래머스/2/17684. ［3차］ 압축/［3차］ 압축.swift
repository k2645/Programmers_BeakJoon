func solution(_ msg:String) -> [Int] {
    
    var dicts = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    
    let msg_arr = Array(msg)
    var ans = [Int]()
    var i = 0
    
    while i < msg_arr.count {
        var str = String(msg_arr[i])
        var code = 0
        while dicts.contains(str) {
            code = dicts.firstIndex(of: str)! + 1
            i += 1
            if i == msg_arr.count { break }
            str += String(msg_arr[i])
        }
        ans.append(code)
        dicts.append(str)
    }
    
    return ans
}