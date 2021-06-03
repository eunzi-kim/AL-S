lottos = [1, 2, 3, 4, 5, 6]
win_nums = [38, 19, 20, 40, 15, 25]

dic = {
    0:6,
    2:5,
    3:4,
    4:3,
    5:2,
    6:1,
}
answer = []

max_cnt = 0
for l in lottos:
    if l == 0:
        max_cnt += 1
    else:
        for w in win_nums:
            if l == w:
                max_cnt += 1

if max_cnt == 0 or max_cnt == 1:
    max_cnt = 0


# print(max_cnt)
# print(dic[max_cnt])
answer.append(dic[max_cnt])
min_cnt = 0
for l in lottos:
    for w in win_nums:
        if l == w:
            min_cnt += 1

if min_cnt == 0 or min_cnt == 1:
    min_cnt = 0

# print(min_cnt)
# print(dic[min_cnt])
answer.append(dic[min_cnt])

print(answer)
