import Foundation

func solution(_ today:String, _ terms:[String], _ privacies:[String]) -> [Int] {
    
    let today_arr = today.components(separatedBy: ".").map { Int($0)! }
    var terms_dic: [String: Int] = [:]
    var result: [Int] = []
    
    for term in terms {
        let arr = term.components(separatedBy: " ").map { $0 }
        terms_dic[arr[0]] = Int(arr[1])
    }
    
    for (idx, privacy) in privacies.enumerated() {
        var expire_date = privacy.components(separatedBy: " ")[0].components(separatedBy: ".").map { Int($0)! }
        let type = privacy.components(separatedBy: " ")[1]
        let term = terms_dic[type]!
        let month = expire_date[1] + term
        
        if month >= 12 {
            if month % 12 == 0 {
                expire_date[1] = 12
                expire_date[0] += month / 12
                expire_date[0] -= 1
            } else {
                expire_date[1] = month % 12
                expire_date[0] += month / 12
            }
        } else {
            expire_date[1] += term
        }
        
        if expire_date[0] == today_arr[0] {
            if expire_date[1] == today_arr[1] {
                if expire_date[2] <= today_arr[2] {
                    result.append(idx + 1)
                }
            } else if expire_date[1] < today_arr[1] {
                result.append(idx + 1)
            }
        } else if expire_date[0] < today_arr[0] {
            result.append(idx + 1)
        }
        
    }
    
    return result
}
