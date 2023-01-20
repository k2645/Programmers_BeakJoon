import Foundation

func solution(_ my_string:String, _ n:Int) -> String {
    
    var my_arr = Array(my_string)
    var result: String = ""
    
    for arr in my_arr {
        result.append(String(repeating: arr, count: n))
    }
    
    return result
}