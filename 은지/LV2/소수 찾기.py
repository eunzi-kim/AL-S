import itertools

def prime(x):
    if x < 2:
        return 0
    else:
        for i in range(2, x):
            if x % i == 0:
                return 0
        return 1

def solution(numbers):
    answer = 0
    a = []
    lst = [str(x) for x in numbers]
    lst.sort(reverse=True)

    arr = [x for x in range(len(lst))]
    for x in itertools.permutations(arr, len(lst)):
        sub_s = ''
        for i in range(len(lst)):
            sub_s += lst[x[i]]
            if prime(int(sub_s)) and int(sub_s) not in a:
                a.append(int(sub_s))
    answer = len(a)
    return answer

numbers = "011"
print(solution(numbers))