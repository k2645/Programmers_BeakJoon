func solution(_ s:String) -> Bool {
    
    guard let num = Int(s) else { return false }
    
    if s.map{ String($0) }.count != 4 && s.map { String($0) }.count != 6 {
        return false
    }
    
    return true
}
