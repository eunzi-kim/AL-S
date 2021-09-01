def solution(m, musicinfos):
    answer = '(None)'
    a = []
    for k in range(len(musicinfos)):
        time = 0
        arr_t = musicinfos[k].split(",")
        t1 = arr_t[0].split(":")
        t2 = arr_t[1].split(":")
        if t1[1] <= t2[1]:
            time = int(t2[1]) - int(t1[1])
        else:
            time = 60 + int(t2[1]) - int(t1[1])
            t2[0] = int(t2[0]) - 1
        time += (int(t2[0]) - int(t1[0])) * 60
        
        musics = []
        sub_v = ''
        for v in arr_t[3]:
            if v != "#":
                if sub_v != '':
                    musics.append(sub_v)
                sub_v = v
            else:
                sub_v += v
                musics.append(sub_v)
                sub_v = ''
        if sub_v != '':
            musics.append(sub_v)

        music = []
        for i in range(time):
            if i >= len(musics):
                i %= len(musics)
            music.append(musics[i])

        mm = []
        sub_v = ''
        for v in m:
            if v != "#":
                if sub_v != '':
                    mm.append(sub_v)
                sub_v = v
            else:
                sub_v += v
                mm.append(sub_v)
                sub_v = ''
        if sub_v != '':
            mm.append(sub_v)

        if len(mm) <= len(music):
            for i in range(len(music)-len(mm)+1):
                if mm == music[i:i+len(mm)]:
                    answer = arr_t[2]
                    a.append([time, len(musicinfos)-k, arr_t[2]])
                    break

    if len(a) > 1:
        a.sort(reverse=True)
        answer = a[0][2]
    return answer

m = "cdcdf"
mi = ["12:00,12:14,HELLO,cdcdcdf", "13:00,13:14,WORLD,ABCDEF"] 
print(solution(m, mi))