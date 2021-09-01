dict = ["0", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

def solution(msg):
    answer = []
    i = past = 0
    while i < len(msg):
        for j in range(i+1, len(msg)+1):
            # 사전에 등록된 글자
            if msg[i:j] in dict:
                past = dict.index(msg[i:j])
                # 마지막으로 처리되지 않은 글자
                if j == len(msg):
                    answer.append(past) # 출력
                    i = j  # 끝
            # 사전에 등록되지 않은 글자
            else:
                answer.append(past) # 출력
                # 사전 추가
                dict.append(msg[i:j])
                i = j-1
                break
    return answer