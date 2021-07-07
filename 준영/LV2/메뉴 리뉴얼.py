from itertools import combinations

def solution(orders, course):
    answer = []
    arr = []
    result = {}
    for order in orders:
        temp = list(order)
        temp.sort()
        for i in course:
            comb_list = combinations(temp, i)
            for j in comb_list:
                if result.get(''.join(j)):
                    result[''.join(j)] = (result[''.join(j)] + 1)
                else:
                    result[''.join(j)] = 1
    for key, value in result.items():
        arr.append([key, value])

    arr.sort(key=lambda x: (len(x[0]), -x[1]))

    for i in course:
        max_i = 2
        temp = []
        for j in arr:
            if len(j[0]) == i:
                if max_i < j[1]:
                    max_i = j[1]
                    temp = [j[0]]
                elif max_i == j[1]:
                    temp.append(j[0])
        
        for k in temp:
            answer.append(k)
    answer.sort()

    return answer


orders = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
course = [2,3,4]
solution(orders, course)
orders = ["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"]
course = [2, 3, 5]
print(solution(orders, course))
orders = ["XYZ", "XWY", "WXA"]
course = [2, 3, 4]
print(solution(orders, course))