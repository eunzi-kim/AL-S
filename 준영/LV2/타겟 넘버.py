result = 0

def dfs(n, numbers, d, target):
    global result
    if n == len(numbers):
        if d == target:
            result += 1
    else:
        for j in [-1, 1]:
            dfs(n+1, numbers, d+(numbers[n]*j), target)


def solution(numbers, target):
    global result 

    dfs(0, numbers, 0, target)

    answer = result
    return answer