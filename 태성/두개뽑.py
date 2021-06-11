
from itertools import combinations


def solution(numbers):
    answer = []

    p_numbers = list(combinations(numbers, 2))
    pre = []
    for a in p_numbers:
        pre.append(sum(a))

    answer = list(set(pre))

    return sorted(answer)