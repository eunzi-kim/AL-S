K, N = map(int, input().split())
arr = [int(input()) for _ in range(K)]

s = 1
e = max(arr)

while s <= e:
    m = (s+e)//2

    cnt = 0
    for x in arr:
        cnt += x // m
    
    if cnt >= N:
        s = m+1
    elif cnt < N:
        e = m-1

print(e)