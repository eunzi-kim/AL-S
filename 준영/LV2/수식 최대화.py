from itertools import permutations

def solution(expression):
    answer = 0
    
    arr = []

    temp = ''
    x = []

    for i in expression:
        if i == '-' or i == '+' or i == '*':
            arr.append(int(temp))
            arr.append(i)
            temp = ''
            if i not in x:
                x.append(i)
        else:
            temp += i

    arr.append(int(temp))


    x_list = permutations(x, len(x))


    for x in x_list:

        arr1 = arr
        temp = []
        skip = False
        for i in x:
            print(temp)
            for j in range(len(arr1)):
                if skip:
                    skip = False
                    continue
                if arr1[j] == i:
                    temp_i = temp.pop()
                    if arr1[j] == '-':
                        temp.append(temp_i - arr1[j+1])
                    elif arr1[j] == '+':
                        temp.append(temp_i + arr1[j+1])
                    elif arr1[j] == '*':
                        temp.append(temp_i * arr1[j+1])
                    skip = True
                else:
                    temp.append(arr1[j])

            if len(temp) == 1:
                answer = max(abs(temp[0]), answer)
            else:
                arr1 = temp
                temp = []

    return answer

expression = "100-200*300-500+20"

print(solution(expression))