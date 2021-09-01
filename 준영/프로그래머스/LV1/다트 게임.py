def solution(dartResult):
    answer = 0
    n = len(dartResult)
    arr = []
    last = 0
    idx = 1
    while idx < n:
        if dartResult[idx].isdigit():
            if dartResult[idx] == '0' and dartResult[idx-1] == '1':
                pass
            else:
                arr.append(dartResult[last:idx])
                last = idx
        idx += 1
    arr.append(dartResult[last:])

    score_arr = [0, 0, 0]

    for i in range(3):
        if arr[i][0] == '1' and arr[i][1] == '0':
            score = 10
            arr[i] = '0' + arr[i][2:]
        else:
            score = int(arr[i][0])
        
        if arr[i][1] == 'S':
            score **= 1
        elif arr[i][1] == 'D':
            score **= 2
        else:
            score **= 3

        if len(arr[i]) >= 3:    
            if i > 0 and arr[i][2] == '*':
                score_arr[i-1] *= 2
                score *= 2
            elif i == 0 and arr[i][2] == '*':
                score *= 2

            if arr[i][2] == '#':
                score *= -1

        score_arr[i] = score

        
    answer = sum(score_arr)
    return answer

print(solution('1S2D*3T'))
print(solution('1D2S#10S'))
print(solution('1D2S0T'))
print(solution('1S*2T*3S'))
print(solution('1D#2S*3S'))
print(solution('1T2D3D#'))
print(solution('1D2S3T*'))