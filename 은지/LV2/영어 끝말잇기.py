def solution(n, words):
    answer = [0, 0]
    past_lst = []
    past = words[0][0]
    for i in range(len(words)):
        # 중복 단어 탐색
        if words[i] not in past_lst:
            past_lst.append(words[i])
        else:
            answer = [i%n+1, i//n+1]
            break

        # 끝말잇기 실패
        if past[-1] != words[i][0]:
            answer = [i%n+1, i//n+1]
            break

        # 과거 단어 변경
        past = words[i]
    return answer

n = 3
w = ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]
print(solution(n, w))