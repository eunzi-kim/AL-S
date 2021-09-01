def two(n):
    if n < 2:
        return n
    else:
        return (n%2) + two(n//2) * 10

def solution(numbers):
    answer = []
    for number in numbers:
        if number % 2 == 0:
            answer.append(number + 1)
        else:
            two_n = str(two(number))
            if len(two_n) == two_n.count("1"):
                v = "10" + two_n[1:]
            else:
                for i in range(len(two_n)-1, -1, -1):
                    if two_n[i-1] == "0" and two_n[i] == "1":
                        v = two_n[:i-1] + "10" + two_n[i+1:]
                        break
            val = 0
            for j in range(len(v)-1, -1, -1):
                val += int(v[j]) * (2 ** (len(v)-j-1))
            answer.append(val)
    return answer