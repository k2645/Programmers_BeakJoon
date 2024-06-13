'''
공집합일 경우엔 j(A, B) = 1
'''
import math

def solution(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()
    
    union = 0
    list1 = {}
    for i in range(len(str1) - 1):
        if str1[i].isalpha() and str1[i + 1].isalpha():
            union += 1
            if str1[i] + str1[i + 1] in list1:
                list1[str1[i] + str1[i + 1]] += 1
            else:
                list1[str1[i] + str1[i + 1]] = 1
            
    list2 = {}
    for i in range(len(str2) - 1):
        if str2[i].isalpha() and str2[i + 1].isalpha():
            union += 1
            if str2[i] + str2[i + 1] in list2:
                list2[str2[i] + str2[i + 1]] += 1
            else:
                list2[str2[i] + str2[i + 1]] = 1
                
    inter = 0
    for k in list1.keys():
        if k in list2:
            inter += min(list1[k], list2[k])
            union -= min(list1[k], list2[k])
    
    if inter == 0 and union == 0:
        return 65536
    else:
        return int((inter / union) * 65536)