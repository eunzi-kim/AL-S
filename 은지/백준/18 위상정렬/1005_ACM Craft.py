import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N, K = map(int, input().split())
    D = list(map(int, input().split()))
    inDegree = [0]*N  # 선수 건물 개수
    Next = [[] for _ in range(N)]  # 자신 다음에 지을 수 있는 건물
    for _ in range(K):
        X, Y = map(int, input().split())
        inDegree[Y-1] += 1
        Next[X-1].append(Y-1)
    W = int(input())-1
    
    time = [0]*N 

    # 미리 지어야하는 건물 없는 경우
    queue = []
    for i in range(N):
        if inDegree[i] == 0:
            queue.append(i)
            time[i] = D[i]
    
    while queue:
        v = queue.pop(0)
        for w in Next[v]:
            if time[w] < time[v] + D[w]:
                time[w] = time[v] + D[w]
            inDegree[w] -= 1
            if inDegree[w] == 0: 
                queue.append(w)            

    print(time[W])