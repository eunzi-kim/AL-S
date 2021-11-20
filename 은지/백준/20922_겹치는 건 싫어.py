import sys
input = sys.stdin.readline

N, K = map(int, input().split())
arr = list(map(int, input().split()))

ans = 0
cnt = [0]*(max(arr)+1)

i = j = 0

while j < N:
    if cnt[arr[j]] < K:        
        cnt[arr[j]] += 1
        if j-i+1 > ans:
            ans = j-i+1
        j += 1
    else:
        cnt[arr[i]] -= 1
        i += 1
    
print(ans)