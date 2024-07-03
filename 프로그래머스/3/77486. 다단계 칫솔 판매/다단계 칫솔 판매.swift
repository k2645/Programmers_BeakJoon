import Foundation

func solution(_ enroll: [String], _ referral: [String], _ seller: [String], _ amount: [Int]) -> [Int] {
    
    var parentDict = [String: String]()
    var priceDict = [String: Int]()
    
    for i in 0..<enroll.count {
        parentDict[enroll[i]] = referral[i]
        priceDict[enroll[i]] = 0
    }
    
    for i in 0..<seller.count {
        var en = seller[i]
        var price = amount[i] * 100
        while en != "-" {
            if price < 10 {
                priceDict[en]! += price
                break
            }
            priceDict[en]! += price - Int(price / 10)
            en = parentDict[en]!
            price = Int(price / 10)
        }
    }
    
    var ans = [Int]()
    
    for i in 0..<enroll.count {
        ans.append(priceDict[enroll[i]]!)
    }
    
    return ans
}