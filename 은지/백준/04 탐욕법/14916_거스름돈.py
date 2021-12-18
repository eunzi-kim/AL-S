n = int(input())

five = n // 5  # 5원 개수
m = n
while True:
    m -= five*5
    if m % 2 and five > 0:
        five -= 1
        m = n  # 초기화
    else:
        if m % 2:
            print(-1)
        else:
            print(five+(m//2))
        break