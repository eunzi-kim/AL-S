import sys
input = sys.stdin.readline

N = int(input())

stack = []

for _ in range(N):
    order = list(input().split())

    if order[0] == "push":
        stack.append(int(order[1]))
    elif order[0] == "pop":
        if len(stack):
            x = stack.pop(-1)
            print(x)
        else:
            print(-1)
    elif order[0] == "size":
        print(len(stack))
    elif order[0] == "empty":
        if len(stack):
            print(0)
        else:
            print(1)
    else:
        if len(stack):
            print(stack[-1])
        else:
            print(-1)