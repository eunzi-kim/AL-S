N = int(input())

three = 0
five = N // 5

while five >= 0:
    # 3킬로그램 봉지와 5킬로그램 봉지로 안 나누어 떨어지는 경우
    if (N - (five * 5)) % 3:
        five -= 1
    # 3킬로그램 봉지와 5킬로그램 봉지로 나누어 떨어지는 경우
    else:
        three = (N - (five * 5)) // 3
        break

print(three + five)