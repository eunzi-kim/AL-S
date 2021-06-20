import string

lowerlst = list(string.ascii_lowercase)

upperlst = list(string.ascii_uppercase)

alllst = lowerlst + upperlst


def solution(s, n):
    answer = ''
    for a in s:
        for i in range(len(lowerlst)):
            if a == lowerlst[i]:
                answer += lowerlst[(i + n) % len(lowerlst)]

        for i in range(len(upperlst)):
            if a == upperlst[i]:
                answer += upperlst[(i + n) % len(upperlst)]

    return answer