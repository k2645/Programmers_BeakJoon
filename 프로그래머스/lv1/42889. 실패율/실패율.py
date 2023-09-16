'''
런타임 에러 -> 시간복잡도 (filter, list, count, sort, for)
'''
def solution(N, stages):
    
    answer = [[i,0] for i in range(1, N + 1)]
    stages_copy = stages
    
    for stage in range(1, N + 1):
        if len(stages_copy) == 0:
            failure = 0
            break
        else:
            failure = stages_copy.count(stage) / len(stages_copy)
        answer[stage - 1][1] = failure
        stages_copy = [i for i in stages_copy if i not in {stage}]
    
    answer.sort(key = lambda x: x[1], reverse = True)
    answer = [t[0] for t in answer]
    
    return answer