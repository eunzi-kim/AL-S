def solution(record):
    record_dit = {}
    answer1 = []
    answer2 = []
    answer = []

    for reco in record:
        temp = reco.split()
        if temp[0] == 'Enter':
            record_dit[temp[1]] = temp[2]
            answer1.append(temp[1])
            answer2.append('님이 들어왔습니다.')
        elif temp[0] == 'Leave':
            answer1.append(temp[1])
            answer2.append('님이 나갔습니다.')
        elif temp[0] == 'Change':
            record_dit[temp[1]] = temp[2]

    for i in range(len(answer2)):
        answer.append(record_dit[answer1[i]] + answer2[i])
    
    return answer