T = int(input())
for _ in range(T):
    ps = input()
    ans = "YES"
    stack = []
    for x in ps:
        if x == "(":
            stack.append("(")
        elif len(stack):
            v = stack.pop(-1)
        else:
            ans = "NO"
            break
    if len(stack):
        ans = "NO"
    print(ans)
