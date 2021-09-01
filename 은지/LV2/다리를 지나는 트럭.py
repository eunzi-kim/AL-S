def solution(bridge_length, weight, truck_weights):
    answer = 0
    # 대기중인 트럭 [남은 시간, 트럭 무게]
    truck_time = []
    for t_w in truck_weights:
        truck_time.append([bridge_length, t_w])
    
    # 다리에 있는 트럭 정보
    now = []
    # 다리에 있는 트럭 무게
    now_weight = 0
    while truck_time:
        answer += 1

        # 다리에 있는 트럭들의 시간 빼주기
        i = 0
        while i < len(now):
            now[i][0] -= 1
            if now[i][0] == 0:
                now_weight -= now[i][1]
                now.pop(i)
            else:
                i += 1

        # 다음 트럭 수용 가능한 경우
        if now_weight + truck_time[0][1] <= weight:
            v = truck_time.pop(0)
            now.append(v)
            now_weight += v[1]

    # 다리에 남아있는 트럭들 처리
    while now:
        answer += 1
        j = 0
        while j < len(now):
            now[j][0] -= 1
            if now[j][0] == 0:
                now_weight -= now[j][1]
                now.pop(j)
            else:
                j += 1

    return answer

b = 100
w = 100
t = [10,10,10,10,10,10,10,10,10,10]
# b = 2
# w = 10
# t = [7,4,5,6]
print(solution(b, w, t))