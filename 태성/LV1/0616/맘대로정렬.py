strings = ["sun", "bed", "car"]

n = 1

def solution(strings, n):
    answer = []

    pre = []
    for s in strings:
        pre.append((s[n], s))

    # print(pre)
    pre = sorted(pre)
    # print(pre)
    for p in pre:
        answer.append(p[1])
    return answer

print(solution(strings, n))