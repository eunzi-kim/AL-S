def solution(n, words):
    answer = [0, 0]
    word_dict = [words[0]]
    idx = 1
    while idx < len(words):
        if word_dict[-1][-1] != words[idx][0] or words[idx] in word_dict:
            answer[0] = (idx % n) + 1
            answer[1] = (idx // n + 1)
            break
        else:
            word_dict.append(words[idx])
        idx += 1

    return answer

n = 3
words = ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]
solution(n, words)