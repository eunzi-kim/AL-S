import sys
input = sys.stdin.readline

N, M = map(int, input().split())

arr = list(map(int, input().split()))

min_tree = 0
max_tree = max(arr)

result = 0

while min_tree <= max_tree:
    middle = (min_tree + max_tree) // 2

    temp = 0

    for i in arr:
        if middle < i:
            temp += i - middle
            if temp > M:
                break

    if temp < M:
        max_tree = middle - 1

    else:
        result = middle
        min_tree = middle + 1

print(result)