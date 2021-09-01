def solution(numbers, target):
    # 더할 수 있는 모든 경우의 수
    arr = []
    for x in numbers:
        n = len(arr)
        if n == 0:
            arr.append(x)
            arr.append(-x)
        else:
            for _ in range(n):
                v = arr.pop(0)
                arr.append(v+x)
                arr.append(v-x)
    # 타겟 추출
    answer = arr.count(target)          
    return answer

numbers = [1, 1, 1, 1, 1]
target = 3
print(solution(numbers, target))