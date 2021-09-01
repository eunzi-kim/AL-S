def solution(msg):
    answer = []
    alphabat = {
        'A': 1,
        'B': 2,
        'C': 3,
        'D': 4,
        'E': 5,
        'F': 6,
        'G': 7,
        'H': 8,
        'I': 9,
        'J': 10,
        'K': 11,
        'L': 12,
        'M': 13,
        'N': 14,
        'O': 15,
        'P': 16,
        'Q': 17,
        'R': 18,
        'S': 19,
        'T': 20,
        'U': 21,
        'V': 22,
        'W': 23,
        'X': 24,
        'Y': 25,
        'Z': 26,
    }

    x = 27
    idx = 0

    while idx < len(msg):
        for i in range(len(msg), idx, -1):
            if alphabat.get(msg[idx:i]):
                answer.append(alphabat.get(msg[idx:i]))
                alphabat[msg[idx:i+1]] = x
                x += 1
                break
            
        idx += len(msg[idx:i])

    return answer

msg = 'KAKAO'
solution(msg)
msg = 'TOBEORNOTTOBEORTOBEORNOT'
solution(msg)
msg = 'ABABABABABABABAB'
solution(msg)