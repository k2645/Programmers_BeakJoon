import Foundation

func solution(_ price:Int, _ money:Int, _ count:Int) -> Int64{
    
    var answer = money
    
    for n in 1...count {
        answer -= n * price
    }
    
    return answer > 0 ? 0 : Int64(-answer)
}
