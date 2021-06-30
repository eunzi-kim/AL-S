def solution(progresses, speeds):
    answer = []
    n = len(progresses)
    arr = [0] * n
    for i in range(n):
        if (100 - progresses[i]) % speeds[i] == 0:
            arr[i] = (100 - progresses[i]) // speeds[i]
        else:
            arr[i] = (100 - progresses[i]) // speeds[i] + 1
    temp = arr[0]
    result = 1
    for i in range(1, n):
        if temp < arr[i]:
            answer.append(result)
            result = 1
            temp = arr[i]
        else:
            result += 1
    answer.append(result)
    return answer