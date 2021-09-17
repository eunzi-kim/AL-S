import sys
input = sys.stdin.readline

arr = []

temp = ''
for i in input().rstrip():
    if i != '.':
        temp += i
    else:
        if temp:
            arr.append(temp)
        arr.append('')
        temp = ''
if temp:
    arr.append(temp)

result = []
for i in arr:
    if i:
        if len(i) % 2:
            print('-1')
            break
        else:
            temp = ''
            temp += 'AAAA'*(len(i)//4)
            if len(i) % 4:
                temp += 'BB'
            result.append(temp)
    else:
        result.append('.')
else:
    print(''.join(result))