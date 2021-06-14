def to_bin(n, x):
    result = ''
    N = n
    n -= 1
    for _ in range(N):
        result += str(x // (2**n))
        x %= (2**n)
        n -= 1
    return result

def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        temp = ""
        x = to_bin(n, arr1[i])
        y = to_bin(n, arr2[i])
        for j in range(n):
            if x[j] == '1' or y[j] == '1':
                temp += "#"
            else:
                temp += " "
                
        answer.append(temp)
            
    return answer

solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28])