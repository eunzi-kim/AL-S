N = int(input())

arr = [True for _ in range(N)]

for i in range(N):
    parenthesis = input()

    stack = []
    for j in parenthesis:
        if j == '(':
            stack.append('(')
        else:
            if len(stack) > 0:
                stack.pop()
            else:
                arr[i] = False
    
    if len(stack) > 0:
        arr[i] = False

for i in arr:
    if i:
        print('YES')
    else:
        print('NO')
