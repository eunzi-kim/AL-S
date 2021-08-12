def solution(m, musicinfos):
    answer = '(None)'
    max_play = 0

    my_note = []

    for i in range(len(m)):
        if m[i] == '#':
            continue

        if i < len(m)-1:
            if m[i+1] == '#':
                my_note.append(m[i]+m[i+1])
            else:
                my_note.append(m[i])
        else:
            my_note.append(m[i])

    for music in musicinfos:
        temp = music.split(',')

        hour1, minute1 = list(map(int, temp[0].split(':')))
        hour2, minute2 = list(map(int, temp[1].split(':')))
        total_minute1 = hour1 * 60 + minute1
        total_minute2 = hour2 * 60 + minute2

        if total_minute1 > total_minute2:
            gap = 24 * 60 - total_minute1 + total_minute2
        else:
            gap = total_minute2 - total_minute1

        note = []

        for i in range(len(temp[3])):
            if temp[3][i] == '#':
                continue

            if i < len(temp[3])-1:
                if temp[3][i+1] == '#':
                    note.append(temp[3][i]+temp[3][i+1])
                else:
                    note.append(temp[3][i])
            else:
                note.append(temp[3][i])

        idx = 0
        result = False
        my_idx = 0

        while idx < gap:
            real_idx = idx % len(note)
            if note[real_idx] == my_note[my_idx]:
                while note[real_idx] == my_note[my_idx]:
                    my_idx += 1
                    real_idx += 1
                    real_idx %= len(note)
                    if my_idx == len(my_note):
                        result = True
                        break
            my_idx = 0

            idx += 1

        if result:
            if max_play < gap:
                answer = temp[2]
                max_play = gap

    return answer

m = "ABCDEFG"
musicinfos = ["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]
solution(m, musicinfos)
m = "CC#BCC#BCC#BCC#B"
musicinfos = ["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"]
solution(m, musicinfos)
