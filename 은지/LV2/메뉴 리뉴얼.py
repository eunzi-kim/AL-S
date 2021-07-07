from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = []
    for c in course:
        menu = []
        for i in range(len(orders)):        
            menu += combinations(sorted(orders[i]), c) 
        info = Counter(menu)

        if info :
            max_v = max(info.values())
            if max_v >= 2:
                for k, v in info.items():
                    if v == max_v:
                        s = "".join(k)
                        answer.append(s)
    answer.sort()
    return answer

o = ["XYZ", "XWY", "WXA"]
c = [2,3,4]
print(solution(o, c))