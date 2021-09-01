def solution(s):
    answer = ''
    dic = {
        'zero': 0,
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,	
        'seven': 7,
        'eight': 8,
        'nine': 9,
    }
    temp = ''
    for i in s:
        if i.isdigit():
            answer += i
        else:
            temp += i
            
            if temp in dic:
                answer += str(dic[temp])
                temp = ''
    answer = int(answer)
    print(answer)
    return answer

s = "one4seveneight123123123123"
solution(s)