def solution(brown, yellow):
    s = brown + yellow
    for x in range(s, 0, -1):
        if s % x == 0:
            w = x
            h = s // x
            if (w-2) * (h-2) == yellow:
                answer = [w, h]
                break
    return answer

b = 10
y = 2
print(solution(b, y))