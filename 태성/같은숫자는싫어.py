arr = [1,1,3,3,0,1,1]

def solution(arr):
    answer = []
    pre = arr[0]

    for i in range(1, len(arr)):
        if arr[i] == pre:
            continue
        else:
            answer.append(pre)
            pre = arr[i]
    answer.append(pre)
    return answer

print(solution(arr))