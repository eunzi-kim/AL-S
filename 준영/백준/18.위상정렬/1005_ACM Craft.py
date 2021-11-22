import sys
input = sys.stdin.readline

T = int(input())

result_arr = []

for TC in range(T):
    N, K = map(int, input().split())

    arr = list(map(int, input().split()))
    arr.insert(0, 0)
    
    graph = [[0 for _ in range(N+1)] for _ in range(N+1)]

    for i in range(K):
        X, Y = map(int, input().split())
        graph[Y][X] = 1
    
    W = int(input())

    visit = [0 for _ in range(N+1)]

    q = []
    result = 0

    if sum(graph[W]) != 0:
        for i in range(1, N+1):
            if graph[W][i] == 1:
                q.append((arr[W], i))
    
        while q:
            t, x = q.pop(0)
            if sum(graph[x]) == 0:
                if result < t + arr[x]:
                    result = t + arr[x]

            if visit[x] < t:
                visit[x] = t

                for i in range(N+1):
                    if graph[x][i] == 1:
                        q.append((t+arr[x], i))
    else:
        result = arr[W]

    result_arr.append(result)

for i in result_arr:
    print(i)

