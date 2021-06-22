def solution(s):
    answer = ''
    arr = []
    for x in s:
        arr.append(x)
    arr.sort(reverse=True)
    answer = "".join(arr)
    return answer