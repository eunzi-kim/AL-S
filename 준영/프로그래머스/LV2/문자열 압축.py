def solution(s):
    answer = len(s)
    
    for n in range(1, len(s)//2+1):
        default_str = ''
        default_n = 1
        temp = s[:n]
        for i in range(n, len(s)+1, n):
            if temp != s[i:i+n]:
                if default_n == 1:
                    default_str += temp
                else:
                    default_str += str(default_n)
                    default_str += temp
                    default_n = 1
                temp = s[i:i+n]
            else:
                default_n += 1
        default_str += s[i:]

        if len(default_str) < answer:
            answer = len(default_str)
    return answer


print(solution('ababcdcdababcdcd'))
