def solution(word):
    answer = 0
    info = {"E": 1, "I": 2, "O": 3, "U": 4}
    for i in range(len(word)):
        if word[i] == "A":
            answer += 1
        else:
            answer += info[word[i]]+1
            for j in range(i+1, 5):
                answer += (5**(5-j))*info[word[i]]

    return answer