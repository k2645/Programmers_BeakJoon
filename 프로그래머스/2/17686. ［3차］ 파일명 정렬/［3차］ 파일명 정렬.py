import re

def solution(files):
    answer = []
    
    file_dict = []
    for file in files:
        num = re.findall(r'\d+', file)
        split_file = file.split(num[0])
        file_dict.append({"name": file,"head": split_file[0].lower(), "num": int(num[0]), "tail": split_file[1]})
    
    for f in sorted(file_dict, key=lambda x: (x["head"], x["num"])):
        answer.append(f["name"])
    
    return answer