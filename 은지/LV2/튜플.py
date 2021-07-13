def solution(s):
    answer = []
    n_lst = [0]*100001
    
    num = ""
    for i in range(len(s)):
        if s[i] != "}" and s[i] != "{" and s[i] != ",":
            num += s[i]
        elif len(num):
            n_lst[int(num)] += 1
            num = ""        

    lst = []
    for i in range(100001):
        if n_lst[i]:
            lst.append((n_lst[i], i))
    lst.sort(reverse=True)
    for x in lst:
        answer.append(x[1])
    return answer

s = "{{20,111},{111}}"
print(solution(s))