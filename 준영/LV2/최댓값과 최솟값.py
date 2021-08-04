def solution(s):
    answer = ''
    arr = list(map(int, s.split()))
    max_i = str(max(arr))
    min_i = str(min(arr))
    answer = min_i + " "+ max_i
    return answer


s = "1 2 3 4"
solution(s)