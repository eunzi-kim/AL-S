N, M = map(int, input().split())

ans = []

def function(i):
    if i == M:
        print(*ans)
        return
    
    for idx in range(1, N+1):
        if len(ans) == 0 or (len(ans) and idx >= ans[-1]):
            ans.append(idx)
            function(i+1)
            ans.pop(-1)

function(0)
