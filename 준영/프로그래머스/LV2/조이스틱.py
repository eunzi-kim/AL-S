def solution(name):
    answer = 0
    list_name = list(name)
    temp = []
    for i in list_name:
        answer += min(ord(i) - ord('A'), (ord('Z') - ord(i) + 1))
        temp.append(min(ord(i) - ord('A'), (ord('Z') - ord(i) + 1)))

     # 왼 오 vs 오 왼
    min_move = 100
    for i in range(1, len(temp)):
        if temp[i] != 0:
            end_point = 0
            for j in range(i, len(temp)):
                if i == j: continue
                if temp[j] != 0:
                    end_point = j
                    break
            
            move_left = len(temp) - j
            move_right = i
            
            min_move = min((move_left*2) + move_right, (move_right*2) + move_left, min_move)

    # 왼 vs 오
    left_move_max = 0
    
    for i in range(1, len(temp)):
        if temp[i] != 0:
            left_move_max = i
            break
    
    right_move_max = 0
    for i in range(len(temp)-1, 1, -1):
        if temp[i] != 0:
            right_move_max = i
            break

    one_move = min(len(temp) - left_move_max, right_move_max)

    answer += min(one_move, min_move)
    return answer

# name = "BBBABB"
# solution(name)
# name = "JEROENA"
# solution(name)
# name = "JAN"
# solution(name)
# name = "BAAAAAAAAAAAAAAAB"
# solution(name)
name = "ZZAAAZZ"
solution(name)
