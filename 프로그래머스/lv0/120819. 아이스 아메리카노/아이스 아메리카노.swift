import Foundation

func solution(_ money:Int) -> [Int] {
    
    let count: Int = money / 5500
    let remainder: Int = money - (count * 5500)
    
    return [count, remainder]
}
