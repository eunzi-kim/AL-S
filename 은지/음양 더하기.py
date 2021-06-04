def solution(absolutes, signs):
    answer = 0
    for i in range(len(absolutes)):
        # true => 양수
        if signs[i]:
            answer += absolutes[i]
        # false => 음수
        else:
            answer -= absolutes[i]
    return answer