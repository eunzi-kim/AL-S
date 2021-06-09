N = 5
stages = [2, 1, 2, 6, 2, 4, 3, 3]


def solution(N, stages):

    # a는 스테이지에 남아있는 인원 카운트 배열
    a = [0]*(N+1)
    # b는 스테이지를 통과한 인원들 카운트 배열
    b = [0]*(N+1)

    for k in stages:
        # 제시된 스테이지(N)을 넘어가는 인원 분기
        if 1<=k<=N:
            a[k] += 1
            for i in range(1, k+1):
                b[i] += 1
        else:
            for j in range(1, len(b)):
                b[j] += 1
    print(a)
    print(b)

    # value로 sort를 하면 그 다음 순위로 값의 순위는 오름차순 유지 이용
    pre = {}

    # 딕셔너리에 실패율 추가
    for n in range(1, N+1):
        pre[n] = a[n]/b[n]

    print(pre)

    # 값을 기준으로 내림차순, 그다음 순위 오름차순 유지
    answer = sorted(pre, key=lambda x: pre[x], reverse=True)

    print(answer)


    return answer


print(solution(N, stages))

# now_tal = pre[0][0]
# same_tal_stage = []
# for i in pre:
#     if now_tal != i[0]:
#         same_tal_stage.sort()
#         answer.extend(same_tal_stage)
#         same_tal_stage = []
#
#         now_tal = i[0]
#         same_tal_stage.append(i[1])
#     else:
#         same_tal_stage.append(i[1])
# same_tal_stage.sort()
# answer.extend(same_tal_stage)