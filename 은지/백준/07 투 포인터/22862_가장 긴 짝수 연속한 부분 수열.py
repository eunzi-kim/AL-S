import sys
input = sys.stdin.readline

N, K = map(int, input().split())
arr = list(map(int, input().split()))

answer = 0
cnt = odd = 0
i = j = 0
while i <= j and j < N:
    if arr[j]%2 == 0:
        cnt += 1
    else:
        odd += 1
    j += 1

    if cnt > answer:
        answer = cnt

    if odd > K:
        if arr[i]%2 == 0:
            cnt -= 1
        else:
            odd -= 1
        i += 1

print(answer)