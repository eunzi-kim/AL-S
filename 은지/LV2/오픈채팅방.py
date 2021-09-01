def solution(record):
    answer = []
    info = {}
    for v in record:
        x = v.split()
        if x[0] != 'Leave':
            info[x[1]] = x[2]
    for v in record:
        x = v.split()
        if x[0] == 'Enter':
            message = info[x[1]] + "님이 들어왔습니다."
            answer.append(message)
        elif x[0] == "Leave":
            message = info[x[1]] + "님이 나갔습니다."
            answer.append(message)
    return answer