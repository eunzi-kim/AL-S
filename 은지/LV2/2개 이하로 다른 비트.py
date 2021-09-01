# 런타임에러

def two(n):
    if n < 2:
        return n
    else:
        return (n%2) + two(n//2) * 10

def solution(numbers):
    answer = []
    for number in numbers:
        num = str(two(number))
        i = 1
        while True:
            sub_n = str(two(number+i))
            while len(sub_n) != len(num):
                m = "0" + num
                num = m
            cnt = 0
            for j in range(len(num)):
                if num[j] != sub_n[j]:
                    cnt += 1
                if cnt > 2:
                    break
            if cnt <= 2:
                answer.append(number+i)
                break
            i += 1
    return answer

n = [2,7]
print(solution(n))