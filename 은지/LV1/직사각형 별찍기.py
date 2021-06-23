a, b = map(int, input().strip().split(' '))
answer = ""
for _ in range(b):
    answer += "*" * a + "\n"
print(answer)