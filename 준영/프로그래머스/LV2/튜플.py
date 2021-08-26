def solution(s):
    answer = []
    arr = s.split('},')
    for i in range(len(arr)):
        arr[i] = arr[i].strip('{')
        arr[i] = arr[i].strip('}')
        arr[i] = list(map(int, arr[i].split(',')))

    arr.sort(key=lambda x: len(x))

    cnt_arr = [0] * 100001
    
    for i in arr:
        for j in i:
            if cnt_arr[j] == 0:
                cnt_arr[j] = 1
                answer.append(j)

    return answer

s = "{{2},{2,1},{2,1,3},{2,1,3,4}}"
solution(s)