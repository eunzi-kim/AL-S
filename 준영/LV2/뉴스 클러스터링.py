import re, math

def solution(str1, str2):
    answer = 0
    p = re.compile('[A-Z]{2}')
    re_str1 = str1.upper()
    re_str2 = str2.upper()

    re_str1_dict = {}
    re_str2_dict = {}

    for i in range(len(re_str1)-1):
        if p.match(re_str1[i:i+2]):
            if re_str1_dict.get(re_str1[i:i+2]):
                re_str1_dict[re_str1[i:i+2]] = re_str1_dict[re_str1[i:i+2]] + 1
            else:
                re_str1_dict[re_str1[i:i+2]] = 1

    for i in range(len(re_str2)-1):
        if p.match(re_str2[i:i+2]):
            if re_str2_dict.get(re_str2[i:i+2]):
                re_str2_dict[re_str2[i:i+2]] = re_str2_dict[re_str2[i:i+2]] + 1
            else:
                re_str2_dict[re_str2[i:i+2]] = 1

    re_str_max = {}
    re_str_min = {}

    for key, value in re_str1_dict.items():
        if re_str2_dict.get(key):
            re_str_max[key] = max(value, re_str2_dict.get(key))
            re_str_min[key] = min(value, re_str2_dict.get(key))
        else:
            re_str_max[key] = value
    
    for key, value in re_str2_dict.items():
        if re_str1_dict.get(key):
            re_str_max[key] = max(value, re_str1_dict.get(key))
        else:
            re_str_max[key] = value
    
    max_val = 0
    for value in re_str_max.values():
        max_val += value
    
    min_val = 0
    for value in re_str_min.values():
        min_val += value
        
    if max_val == 0:
        answer = 65536
    else:
        answer = 65536 * (min_val / max_val)
        answer = math.trunc(answer)

    return answer

str1 = 'FRANCE'
str2 = 'french'
solution(str1, str2)
str1 = 'aa1+aa2'
str2 = 'AAAA12'
solution(str1, str2)
str1 = 'handshake'
str2 = 'shakehands'
solution(str1, str2)