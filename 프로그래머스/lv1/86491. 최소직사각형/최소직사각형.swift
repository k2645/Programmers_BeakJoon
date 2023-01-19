import Foundation

func solution(_ sizes:[[Int]]) -> Int {
    
    var width: [Int] = []
    var height: [Int] = []
    
    for size in sizes {
        if size[0] > size[1] {
            width.append(size[0])
            height.append(size[1])
        } else {
            width.append(size[1])
            height.append(size[0])
        }
    }
    
    let result = width.max()! * height.max()!
    
    return result
    
}