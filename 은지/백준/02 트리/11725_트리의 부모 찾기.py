import sys
input = sys.stdin.readline

N = int(input())

d = [[] for _ in range(N+1)]

for _ in range(N-1):
    s, e = map(int, input().split())
    d[s].append(e)
    d[e].append(s)

chk = [0] * (N+1)
answer = [0] * (N+1) # 부모 넣기
stack = [1]
chk[1] = 1
while stack:
    v = stack.pop(0)
    for w in d[v]:
        if chk[w] == 0:
            stack.append(w)
            chk[w] = 1
            answer[w] = v

for i in range(2, N+1):
    print(answer[i])