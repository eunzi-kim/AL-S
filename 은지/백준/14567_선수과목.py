import sys
input = sys.stdin.readline

N, M = map(int, input().split())

rank = [0] * (N+1)
indegree = [0] * (N+1)  # 선수과목 개수
child = [[] for _ in range(N+1)]  # 배울 수 있는 과목

for _ in range(M):
    A, B = map(int, input().split())
    child[A].append(B)  # 배울 수 있는 과목 추가
    indegree[B] += 1  # 선수과목 개수 추가

queue = []

# 선수과목 필요없는 과목들
for i in range(1, N+1):
    if indegree[i] == 0:
        rank[i] = 1
        queue.append(i)

# 바로 다음 배우는 과목 탐색
while queue:
    v = queue.pop(0)
    for w in child[v]:
        if indegree[w] == 1:
            rank[w] = rank[v]+1  # w는 v 바로 다음 배우는 과목
            queue.append(w)
        indegree[w] -= 1  # 선수과목 1개 살펴봄

print(*rank[1:])