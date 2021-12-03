T = int(input())

for _ in range(T):
    
    s = input()

    cnt = [0]*26
    max_v = 0

    for x in s:
        if x != " ":
            i = ord(x)-97
            cnt[i] += 1
            if cnt[i] > max_v:
                max_v = cnt[i]

    if cnt.count(max_v) > 1:
        print("?")
    else:
        j = cnt.index(max_v)
        print(chr(j+97))