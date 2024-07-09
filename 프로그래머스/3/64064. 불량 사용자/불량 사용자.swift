/*
개수 세기..
dfs?
*/

import Foundation

func isPossible(_ user: [String], _ banned: [String]) -> Bool {
    if user.count == banned.count {
        for i in 0..<user.count {
            if banned[i] != "*" && user[i] != banned[i] {
                return false
            }
        }
        return true
    } else {
        return false
    }
}

func solution(_ user_id:[String], _ banned_id:[String]) -> Int {
    
    var userDict = [String:[String]]()
    for bannedId in banned_id {
        userDict[bannedId] = []
        for userId in user_id {
            if isPossible(Array(userId).map { String($0) }, Array(bannedId).map { String($0) }) {
                userDict[bannedId]!.append(userId)
            }
        }
    }
    print(userDict)
    
    var result = [Set<String>]()
    
    func makeBanned(_ bannedIdx: Int, _ bannedArr: [String]) {
        if bannedArr.count == banned_id.count {
            if !result.contains(Set(bannedArr)) {
                result.append(Set(bannedArr))
            }
            return
        }

        for id in userDict[banned_id[bannedIdx]]! {
            if !bannedArr.contains(id) {
                makeBanned(bannedIdx + 1, bannedArr + [id])
            }
        }
    }
    
    makeBanned(0, [])
    
    return result.count
}