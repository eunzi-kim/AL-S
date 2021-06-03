def solution(array, commands):
    answer = []
    for i in range(len(commands)):
        a = commands[i]
        b = array[(a[0]-1):(a[1]):1]
        b.sort()
        answer.append(b[(a[2]-1)])
    return answer