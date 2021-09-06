import itertools

N, M = map(int, input().split())

arr = [x for x in range(1, N+1)]
v = itertools.permutations(arr, M)

for w in v:
    sub_a = ""
    for i in range(M):
        sub_a += str(w[i]) + " "
    print(sub_a)


######################################


N, M = map(int, input().split())

visited = [0]*N
ans = []

def seq():
    if len(ans) == M:
        answer = ""
        for x in ans:
            answer += str(x) + " "
        print(answer)
        return
    
    for i in range(N):
        if visited[i] == 0:
            visited[i] = 1
            ans.append(i+1)
            seq()
            visited[i] = 0
            ans.pop(-1)

seq()