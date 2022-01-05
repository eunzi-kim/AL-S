N, M = map(int, input().split())
arr = [input() for _ in range(N)]

example = ["A", "C", "G", "T"]
cnt = [0]*4
ans = ""
sum_v = 0

for j in range(M):
    for i in range(N):
        idx = example.index(arr[i][j])
        cnt[idx] += 1
    
    max_v = max(cnt)
    max_i = cnt.index(max_v)
    ans += example[max_i]
    sum_v += N-max_v

    cnt = [0]*4

print(ans)
print(sum_v)