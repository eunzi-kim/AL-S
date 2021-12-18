import sys
input = sys.stdin.readline

A = int(input())  # 사람 수
T = int(input())  # 구호 번째
aid = int(input())  # 구호 이름

n = 2  # 뻔 데기 반복 개수
cnt_f = cnt_d = n  # 뻔 데기 카운트
person = 0  # 현재 사람
i = 0
cnt = 0
temp = 1

while cnt < T:
    if i < 4:
        if temp: temp = 0
        else: temp = 1

    else:
        if cnt_f > 0:
            cnt_f -= 1
            temp = 0
        elif cnt_d > 0:
            cnt_d -= 1
            temp = 1

    if aid == temp:
        cnt += 1

    if cnt == T:
        break
    else:
        person = (person + 1) % A
        i += 1
        if cnt_f == 0 and cnt_d == 0:
            n += 1
            cnt_f = cnt_d = n
            i = 0

print(person)