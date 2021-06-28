from itertools import combinations

def solution(numbers):
    arr = list(set(map(sum, combinations(numbers, 2))))
    arr.sort()
    return arr

solution([2,1,3,4,1])