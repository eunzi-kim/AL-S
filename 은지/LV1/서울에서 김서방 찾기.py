def solution(seoul):
    answer = ''
    for x in range(len(seoul)):
        if seoul[x] == 'Kim':
            answer += '김서방은 ' + str(x) + '에 있다'
    return answer