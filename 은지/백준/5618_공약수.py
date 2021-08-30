n = int(input())
numbers = list(map(int, input().split()))

for x in range(1, min(numbers)+1):
    for number in numbers:
        if number % x:
            break
    else:
        print(x)