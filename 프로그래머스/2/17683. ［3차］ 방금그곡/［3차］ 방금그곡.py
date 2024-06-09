import math

def replace_string(string):
    result = string.replace("C#", "c")
    result = result.replace("D#", "d")
    result = result.replace("F#", "f")
    result = result.replace("G#", "g")
    result = result.replace("A#", "a")
    result = result.replace("B#", "b")
    
    return result

def solution(m, musicinfos):
    answer = "(None)"
    time = 0
    m = replace_string(m)
    for info in musicinfos:
        info_list = info.split(',')
        music_code = replace_string(info_list[3])
        start = list(map(int, info_list[0].split(':')))
        start = start[0] * 60 + start[1]
        end = list(map(int, info_list[1].split(':')))
        end = end[0] * 60 + end[1]
        music_code = list(music_code * math.ceil((end - start) / len(music_code)))
        while len(music_code) > end - start:
            music_code.pop()
        music_code = "".join(music_code)
        if m in music_code and end - start > time:
            answer = info_list[2]
            time = end - start
    
    return answer
