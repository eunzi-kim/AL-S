def solution(numbers):
    answer = []
    for n in numbers:
        temp = []
        
        while n:
            temp.append(n % 2)
            n //= 2

        temp.append(0)

        for i in range(len(temp)):
            if i == 0 and temp[i] == 0:
                temp[i] = 1
                break

            if temp[i] == 0:
                temp[i-1] = 0
                temp[i] = 1
                break
        
        t = 0
        s = 1

        for i in temp:
            t += i * s
            s *= 2

        answer.append(t)
    return answer

numbers = [2, 7]
solution(numbers)