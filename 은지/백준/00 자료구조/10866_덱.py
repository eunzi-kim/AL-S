import sys
input = sys.stdin.readline

N = int(input())
deq = []
for _ in range(N):
    order = input().split()
    if order[0] == "push_front":
        deq = [order[1]] + deq
    elif order[0] == "push_back":
        deq.append(order[1])
    elif order[0] == "pop_front":
        if len(deq):
            print(deq[0])
            deq.pop(0)
        else:
            print(-1)
    elif order[0] == "pop_back":
        if len(deq):
            print(deq[-1])
            deq.pop(-1)
        else:
            print(-1)
    elif order[0] == "size":
        print(len(deq))
    elif order[0] == "empty":
        if len(deq):
            print(0)
        else:
            print(1)
    elif order[0] == "front":
        if len(deq):
            print(deq[0])
        else:
            print(-1)
    elif order[0] == "back":
        if len(deq):
            print(deq[-1])
        else:
            print(-1)
            