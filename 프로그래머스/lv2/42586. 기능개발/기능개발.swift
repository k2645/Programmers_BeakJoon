import Foundation

func solution(_ progresses:[Int], _ speeds:[Int]) -> [Int] {
    
    var ans: [Int] = []
    var publishes: [Int] = []
    
    for (idx, progress) in progresses.enumerated() {
        let speed = speeds[idx]
        
        if (100 - progress) % speed == 0 {
            publishes.append((100 - progress) / speed)
        } else {
            publishes.append((100 - progress) / speed + 1)
        }
    }
    
    var publish_day = publishes[0]
    var count: Int = 0
    
    for publish in publishes {
        if publish > publish_day {
            ans.append(count)
            publish_day = publish
            count = 1
        } else {
            count += 1
        }
    }
    ans.append(count)
    
    return ans
}
