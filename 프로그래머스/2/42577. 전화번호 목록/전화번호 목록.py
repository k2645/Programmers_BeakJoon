def solution(phone_book):
    answer = True
    
    phone_book = sorted(phone_book, key = len)
    
    length = [len(phone_book[0])]
    
    phone_dict = {}
    
    for num in phone_book:
        for i in length:
            if num[:i] in phone_dict:
                answer = False
                break
            elif len(num) == i:
                phone_dict[num] = num
            elif len(num) != length[-1]:
                length.append(len(num))
    
    return answer