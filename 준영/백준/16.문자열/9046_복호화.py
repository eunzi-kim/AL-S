N = int(input())

for i in range(N):
    secret = input()
    result = ''
    
    cnt = 0

    for i in secret:
        if i == ' ':
            continue

        if secret.count(i) > cnt:
            cnt = secret.count(i)
            result = i
        
        elif result != i and secret.count(i) == cnt:
            result = '?'

    print(result)
