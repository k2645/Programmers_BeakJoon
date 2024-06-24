import Foundation

func solution(_ fees:[Int], _ records:[String]) -> [Int] {
    
    let inout_info = records.map { $0.split(separator: " ") }
    var park_time = [String:Int]()
    var park_total_time = [String:Int]()
    
    for info in inout_info {
        let times = info[0].split(separator: ":")
        let time = Int(times[0])! * 60 + Int(times[1])!
        let car_num = String(info[1])
        if info[2] == "IN" {
            park_time[car_num] = time
        } else {
            if park_total_time[car_num] == nil {
                park_total_time[car_num] = time - park_time[car_num]!
            } else {
                park_total_time[car_num]! += time - park_time[car_num]!
            }
            park_time[car_num] = nil
        }
    }
    
    let last_time = (23 * 60) + 59
    for (car_num, time) in park_time {
        if park_total_time[car_num] == nil {
            park_total_time[car_num] = last_time - time
        } else{
            park_total_time[car_num]! += last_time - time
        }
    }
    
    var park_price = [String:Double]()
    for (car_num, time) in park_total_time {
        park_price[car_num] = Double(fees[1])
        if time > fees[0] {
            park_price[car_num]! += ceil(Double(time - fees[0]) / Double(fees[2])) * Double(fees[3])
        }
    }
    
    var ans = [Int]()
    for num in park_price.keys.sorted() {
        ans.append(Int(park_price[num]!))
    }
    
    return ans
}