def solution(bridge_length, weight, truck_weights):
    bridge_arr = [0] * bridge_length
    N = len(truck_weights)
    bridge_arr.pop(0)
    bridge_arr.append(truck_weights[0])
    time = 1
    idx = 1
    while (idx < N) or (sum(bridge_arr) > 0):
        time += 1
        bridge_arr.pop(0)
        if idx >= N:
            bridge_arr.append(0)
        else:
            if sum(bridge_arr) + truck_weights[idx] <= weight:
                bridge_arr.append(truck_weights[idx])
                idx += 1
            else:
                bridge_arr.append(0)
        
    return time

bridge_length = 2
weight = 10
truck_weights = [7,4,5,6]
solution(bridge_length, weight, truck_weights)