def solution(N, road, K):
    answer = 0  
    g = [[] for _ in range(N+1)]
    d = [500001] * (N+1)
    d[1] = 0

    for r in road:
        g[r[0]].append([r[0], r[1], r[2]])
        g[r[1]].append([r[1], r[0], r[2]])

    queue = g[1]
    while queue:
        v = queue.pop(0)
        s = v[0]
        e = v[1]
        dis = v[2]

        if d[e] > d[s] + dis:
            d[e] = d[s] + dis
            for w in g[e]:
                queue.append(w)
    
    for i in range(1, N+1):
        if d[i] <= K:
            answer += 1
    return answer

n = 5
r = [[2, 3, 3], [5, 2, 2], [1, 4, 2], [5, 3, 1], [5, 4, 2], [1, 2, 1] ]
k = 3
print(solution(n, r, k))