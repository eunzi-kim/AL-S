def solution(N, road, K):
    answer = 0

    INF = int(1e9)
    
    result_arr = [INF] * (N+1)
    result_arr[1] = 0

    road_two = [[10001 for _ in range(N+1)] for _ in range(N+1)]

    for i in road:
        if road_two[i[0]][i[1]] > i[2]:
            road_two[i[0]][i[1]] = i[2]
            road_two[i[1]][i[0]] = i[2]
    
    # dijkstra

    my_queue = []
    my_queue.append((0, 1))
    while my_queue:
        my_queue.sort(key=lambda x: x[0])
        dist, now = my_queue.pop(0)

        if result_arr[now] < dist:
            continue

        for i in range(N+1):
            if road_two[now][i] < 10001:
                cost = dist + road_two[now][i]
                
                if cost < result_arr[i]:
                    result_arr[i] = cost
                    my_queue.append((cost, i))

    for i in result_arr:
        if i <= K:
            answer += 1

    return answer


N = 5
road = [[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]]
K = 3
solution(N, road, K)