num = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]

def change(x, n):
    q, r = divmod(x, n)
    if q == 0:
        return num[r]
    else:
        return change(q, n) + num[r]

def solution(n, t, m, p):
    answer = ''
    
    all_ans = ''
    i = 0
    while len(all_ans) <= t*m:
        all_ans += str(change(i, n))
        i += 1
    
    i = p-1
    while len(answer) < t:
        answer += all_ans[i]
        i += m

    return answer