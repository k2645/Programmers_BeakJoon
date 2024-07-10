/*
expression -> [Int]
모든 경우의 수를 계산하고 그 중 가장 큰 값을 내뱉는다
어떻게 계산? stack을 이용해서 계산?
*/

import Foundation

enum Operator: String {
    case multi
    case sum
    case sub
}

func calculate(_ nums: [Int], _ operators: [Operator], _ operatorOrder: [Operator]) -> Int64 {
    
    var numStack = nums
    var operatorStack = operators
    
    for orderOper in operatorOrder {
        var newNumStack = [Int]() + [numStack.removeFirst()]
        var newOperatorStack = [Operator]()
        for oper in operatorStack {
            if oper.rawValue != orderOper.rawValue {
                newNumStack.append(numStack.removeFirst())
                newOperatorStack.append(oper)
            } else {
                let new = newNumStack.popLast()!
                let old = numStack.removeFirst()
                switch oper {
                    case .multi: newNumStack.append(new * old)
                    case .sum: newNumStack.append(new + old)
                    case .sub: newNumStack.append(new - old)
                }
            }
        }
        numStack = newNumStack
        operatorStack = newOperatorStack
    }
    
    return Int64(abs(numStack[0]))
}

func permutation(_ array: [Operator], _ n: Int) -> [[Operator]] {
    var result = [[Operator]]()
    if array.count < n { return result }

    var visited = Array(repeating: false, count: array.count)
    
    func cycle(_ now: [Operator]) {
        if now.count == n {
            result.append(now)
            return
        }
        
        for i in 0..<array.count {
            if visited[i] {
                continue
            } else {
                visited[i] = true
                cycle(now + [array[i]])
                visited[i] = false
            }
        }
    }
    
    cycle([])
    
    return result
}

func solution(_ expression:String) -> Int64 {
    
    let numArr = expression.components(separatedBy: ["*", "+", "-"]).map { Int($0)! }
    var operatorArr = [Operator]()
    expression.components(separatedBy: ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]).filter { $0 != "" }.forEach {
        if $0 == "*" {
            operatorArr.append(Operator.multi)
        } else if $0 == "+" {
            operatorArr.append(Operator.sum)
        } else {
            operatorArr.append(Operator.sub)
        }
    }
    let operSet = Array(Set(operatorArr))
    var result = [Int64]()
    for per in permutation(operSet, operSet.count) {
        result.append(calculate(numArr, operatorArr, per))
    }
    
    return result.max()!
}