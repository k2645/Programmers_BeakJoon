func solution(_ phone_number:String) -> String {
    
    if phone_number.count == 4 { return phone_number }
    
    var phoneArr = phone_number.map { String($0) }
    let arrCnt = phone_number.count - 4
    
    for idx in 0..<arrCnt {
        phoneArr[idx] = "*"
    }
    
    return phoneArr.joined()
}
