def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b / gcd(a, b)

def solution(arr):
    temp = arr[:]

    while len(temp) > 1:
        lcm_arr = []
        x = temp[0]

        for i in temp[1:]:
            lcm_arr.append(lcm(x, i))
        
        temp = lcm_arr

    answer = temp.pop()

    return answer

arr = [2,6,8,14]
solution(arr)