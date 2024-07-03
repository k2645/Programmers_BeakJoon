import Foundation

func isValid(_ strArr: [String]) -> Bool {
    
    var stack = [String]()
    for s in strArr {
        if let str = stack.last { // stack 안에 값이 있는 경우
            if s == "[" || s == "(" || s == "{" {
                stack.append(s)
            } else if (str == "[" && s == "]") || (str == "{" && s == "}") || (str == "(" && s == ")") {
                let _ = stack.popLast()
            } else {
                return false
            }
        } else {
            if s == "]" || s == ")" || s == "}" {
                return false
            } else {
                stack.append(s)
            }
        }
    }
    
    if stack.isEmpty {
        return true
    } else {
        return false
    }
}

func solution(_ s:String) -> Int {
    
    var strArr = s[s.startIndex...]
    var ans = 0
    for _ in 0..<strArr.count {
        if isValid(Array(strArr).map { String($0) }) {
            ans += 1
        }
        let str = strArr.popFirst()!
        strArr.append(str)
    }
    
    return ans
}