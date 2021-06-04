def solution(nums):
    answer = 0
    N = len(nums) // 2
    # 폰켓몬의 종류
    mon = []
    for x in nums:
        if x not in mon:
            mon.append(x)
    # 폰켓몬의 종류 수 < 가져갈 수 있는 폰켓몬의 수
    if len(mon) < N:
        answer = len(mon)
    # 폰켓몬의 종류 수 >= 가져갈 수 있는 폰켓몬의 수
    else:
        answer = N
    return answer