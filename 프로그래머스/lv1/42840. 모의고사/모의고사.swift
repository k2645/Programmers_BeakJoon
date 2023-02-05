import Foundation

func solution(_ answers:[Int]) -> [Int] {
    
    var cnt = [0, 0, 0]
    var result: [Int] = []
    
    for (idx, answer) in answers.enumerated() {
        var answer1 = 1
        var answer2 = 1
        var answer3 = 1
        
        switch (idx + 1) % 5 {
        case 0: answer1 = 5
        default: answer1 = (idx + 1) % 5
        }
        
        if (idx + 1) % 2 == 1 {
            answer2 = 2
        } else {
            switch ((idx + 1) / 2) % 4 {
            case 1: answer2 = 1
            case 2: answer2 = 3
            case 3: answer2 = 4
            default: answer2 = 5
            }
        }
        
        switch (idx + 1) % 10 {
        case 1, 2: answer3 = 3
        case 3, 4: answer3 = 1
        case 5, 6: answer3 = 2
        case 7, 8: answer3 = 4
        default: answer3 = 5
        }
        
        if answer == answer1 { cnt[0] += 1 }
        if answer == answer2 { cnt[1] += 1 }
        if answer == answer3 { cnt[2] += 1 }
        
    }
    
    for i in 0..<3 {
        if cnt.max()! == cnt[i] {
            result.append(i + 1)
        }
    }
    
    return result
}
