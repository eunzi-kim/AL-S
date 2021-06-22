n = 118372


def solution(n):
    answer = 0
    s_n = str(n)
    tmp = []
    for s in s_n:
        tmp.append(int(s))

    sort_tmp = sorted(tmp, reverse=True)
    print(sort_tmp)
    s_sort_tmp = list(map(str, sort_tmp))
    print(s_sort_tmp)
    answer = ''.join(s_sort_tmp)
    return answer

print(solution(n))