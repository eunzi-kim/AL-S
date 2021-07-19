def solution(s):
    answer = ""
    num = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    n = ""
    for v in s:
        if v.isdigit():
            answer += v
        else:
            n += v

        if n in num:
            for i in range(10):
                if n == num[i]:
                    answer += str(i)
            n = ""

    answer = int(answer)
    return answer

s = "zeroone"
print(solution(s))