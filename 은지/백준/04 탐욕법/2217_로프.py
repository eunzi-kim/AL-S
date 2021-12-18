import sys
input = sys.stdin.readline

N = int(input())
arr = []
for _ in range(N):
    w = int(input())
    arr.append(w)

arr.sort()

ans = 0
for i in range(N):
    # (로프 개수) * (분산될 중량)
    if ans < (N-i)*arr[i]:
        ans = (N-i)*arr[i]
    
print(ans)