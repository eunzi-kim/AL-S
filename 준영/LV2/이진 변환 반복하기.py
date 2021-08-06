def solution(s):
    answer = []
    cnt = 0
    zero_cnt = 0

    s_arr = list(map(int, s))
    
    while len(s_arr) > 1:

        idx = 0

        while len(s_arr) > idx:
            if s_arr[idx] == 0:
                s_arr.pop(idx)
                zero_cnt += 1
            else:
                idx += 1

        
        n = len(s_arr)

        new_arr = []

        while n:
            new_arr.append(n % 2)
            n //= 2

        s_arr = new_arr
        cnt += 1
    answer = [cnt, zero_cnt]
    return answer


s = "110010101001"
solution(s)