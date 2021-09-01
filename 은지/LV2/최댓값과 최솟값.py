def solution(s):
    numbers = []
    sub = ""
    for v in s:
        if v != " ":
            sub += v
        else:
            numbers.append(int(sub))
            sub = ""
    numbers.append(int(sub))
    answer = str(min(numbers)) + " " + str(max(numbers))
    return answer

s = "1 2 3 4"
print(solution(s))