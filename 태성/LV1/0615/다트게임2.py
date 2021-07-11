dartResult = "1S2D*3T"

def solution(dartResult):
    answer = 0

    pre = []
    tmp = ""
    for d in dartResult:
        if d not in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            if tmp:
                pre.append(int(tmp))
                tmp = ""
                pre.append(d)
            else:
                pre.append(d)
        else:
            tmp += d
    print(pre)


    array = []

    for p in pre:
        if p in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
            if len(array) < 2:
                array.append(p)
            else:
                answer += array.pop(0)
                array.append(p)

        else:
            if p == "S":
               continue

            elif p == "D":
                dd = array.pop()
                array.append(dd * dd)

            elif p == "T":
                t = array.pop()
                array.append(t * t * t)


            elif p == "*":
                if len(array) == 1:
                    j = array.pop()
                    array.append(j * 2)
                elif len(array) == 2:
                    j = array.pop()
                    jj = array.pop()

                    array.append(jj * 2)
                    array.append(j * 2)

            elif p == "#":
                z = array.pop()
                array.append(z * (-1))

    for a in array:
        answer += a


    return answer

print(solution(dartResult))