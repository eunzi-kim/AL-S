def solution(numbers, hand):
    answer = ''
    keypad = [[3, 1]]

    for i in range(3):
        for j in range(3):
            keypad.append([i, j])
            
    left_hand = [3, 0]
    right_hand = [3, 2]

    for i in numbers:
        x, y = keypad[i]
        if i in (2, 5, 8, 0):
            left_d = abs(left_hand[0] - x) + abs(left_hand[1] - y)
            right_d = abs(right_hand[0] - x) + abs(right_hand[1] - y)
            if left_d < right_d:
                left_hand = [x, y]
                answer += "L"
            elif left_d > right_d:
                right_hand = [x, y]
                answer += "R"
            else:
                if hand == "right":
                    right_hand = [x, y]
                    answer += "R"
                else:
                    left_hand = [x, y]
                    answer += "L"
        elif i in (1, 4, 7):
            left_hand = [x, y]
            answer += "L"
        else:
            right_hand = [x, y]
            answer += "R"
        
    return answer


numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]	
hand = "right"
print(solution(numbers, hand))