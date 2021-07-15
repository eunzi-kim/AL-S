import itertools
import copy

def solution(expression):
    answer = 0
    # 숫자, 기호 정리
    stack_n = []
    stack_s = []
    num = ""
    for e in expression:
        if e == "-":
            stack_n.append(int(num))
            num = ""
            stack_s.append(e)
        elif e == "+":
            stack_n.append(int(num))
            num = ""
            stack_s.append(e)
        elif e == "*":
            stack_n.append(int(num))
            num = ""
            stack_s.append(e)
        else:
            num += e
    stack_n.append(int(num))

    # 모든 경우의 수 계산하며 최대값 탐색
    symbol = ["*", "+", "-"]
    for v in itertools.permutations(symbol, 3):
        stack_ss = copy.deepcopy(stack_s)
        stack_nn = copy.deepcopy(stack_n)
        for j in range(3):
            i = 0
            while i < len(stack_ss):
                if len(stack_nn) == 1:
                    break
                if stack_ss[i] == v[j]:
                    w = stack_nn.pop(i+1)
                    stack_ss.pop(i)
                    if v[j] == "*":
                        stack_nn[i] = stack_nn[i] * w
                    elif v[j] == "+":
                        stack_nn[i] = stack_nn[i] + w
                    elif v[j] == "-":
                        stack_nn[i] = stack_nn[i] - w
                else:
                    i += 1
        if answer < abs(stack_nn[0]):
            answer = abs(stack_nn[0])
    return answer

e = "100-200*300-500+20"
print(solution(e))