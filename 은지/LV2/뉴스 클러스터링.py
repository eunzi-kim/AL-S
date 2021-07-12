def solution(str1, str2):
    str1 = str1.upper()
    str2 = str2.upper()
    a = []
    b = []
    for i in range(len(str1)-1):
        if 65 <= ord(str1[i]) <= 90 and 65 <= ord(str1[i+1]) <= 90:
            a.append(str1[i:i+2])
    for j in range(len(str2)-1):
        if 65 <= ord(str2[j]) <= 90 and 65 <= ord(str2[j+1]) <= 90:
            b.append(str2[j:j+2])

    inter = 0
    a.sort()
    b.sort()
    i = j = 0
    while i < len(a) and j < len(b):
        if a[i] == b[j]:
            inter += 1
            i += 1
            j += 1
        elif a[i] < b[j]:
            i += 1
        else:
            j += 1
    union = len(a) + len(b) - inter
    
    if union == 0:
        answer = 65536
    else:
        answer = int((inter / union)*65536)
    return answer

# print(ord("a"), ord("z"), ord("A"), ord("Z"))