def solution(answers):
    answer = []
    number_one = [1, 2, 3, 4, 5]
    number_two = [1, 3, 4, 5]
    number_three = [3, 1, 2, 4, 5]

    one_idx = 0
    two_idx = 0
    three_idx = 0

    # 맞은 개수 저장하는 배열
    numbers = [0] * 3

    for i in answers:
        # 1번
        if number_one[one_idx] == i:
            numbers[0] += 1

        one_idx += 1
        if one_idx == 5: one_idx = 0

        # 2번
        if two_idx % 2 == 0:
            if i == 2:
                numbers[1] += 1
            
        else:
            if number_two[two_idx//2] == i:
                numbers[1] += 1

        two_idx += 1
        if two_idx == 8: two_idx = 0

        # 3번
        if number_three[three_idx//2] == i:
            numbers[2] += 1

        three_idx += 1
        if three_idx == 10: three_idx = 0
            
    for i in range(3):
        if max(numbers) == numbers[i]:
            answer.append(i+1)
            
    return answer


answer = [1,2,3,4,5]

solution(answer)

answer = [1,3,2,4,2]

solution(answer)