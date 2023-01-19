import Foundation

func solution(_ survey:[String], _ choices:[Int]) -> String {
    
    var type_score = [["R": 0, "T": 0],
                      ["C": 0, "F": 0],
                      ["J": 0, "M": 0],
                      ["A": 0, "N": 0]]
    
    for (index,type) in survey.enumerated() {
        switch type {
        case "RT", "TR":
            type_score[0] = calPoint(type, type_score[0], choices[index])
        case "CF", "FC":
            type_score[1] = calPoint(type, type_score[1], choices[index])
        case "JM", "MJ":
            type_score[2] = calPoint(type, type_score[2], choices[index])
        default:
            type_score[3] = calPoint(type, type_score[3], choices[index])
        }
    }
    
    var result: String = ""
    
    for types in type_score {
        
        var type_name = "Z"
        let mx_point = types.values.max()
        
        for (type, point) in types {
            if point == mx_point && type_name > type {
                type_name = type
            }
        }
        
        result.append(type_name)
    }
    
    return result
}

func calPoint(_ type: String, _ point: [String: Int], _ choice: Int) -> [String: Int] {
    
    var newPoint = point
    let first_type = String(type[type.startIndex])
    let last_type = String(type[type.index(before: type.endIndex)])
    
    switch choice {
    case 1...3:
        newPoint[first_type]! += 4 - choice
    case 5...7:
        newPoint[last_type]! += choice - 4
    default:
        break
    }
    
    return newPoint
    
}
