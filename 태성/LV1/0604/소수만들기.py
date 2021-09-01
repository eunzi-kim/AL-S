def solution(nums):
    answer = 0

    pre = []
    for i in range(len(nums) - 2):
        # pre.append(nums[i])
        for j in range(i + 1, len(nums) - 1):
            # pre.append(nums[j])
            for k in range(j + 1, len(nums)):
                pre.append(nums[i] + nums[j] + nums[k])

    # print(pre)
    chk = []
    for p in pre:
        for i in range(2, (p // 2) + 1):
            if p%i == 0:
                chk.append(p)
                break
    answer = len(pre) - len(chk)
    return answer