def solution(files):
    answer = []
    F = []
    for i in range(len(files)):
        chk = 0
        sub_s = ""
        sub_n = ""
        for file in files[i]:
            if 48 <= ord(file) <= 57:
                sub_n += file
                chk = 1
            elif chk == 0:
                sub_s += file
            else:
                break
        F.append([sub_s.lower(), int(sub_n), i])

    F.sort()

    for i in range(len(F)):
        answer.append(files[F[i][2]])
            
    return answer
