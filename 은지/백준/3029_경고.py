current = input()
goal = input()

c_h = int(current[0:2])
c_m = int(current[3:5])
c_mm = int(current[6:])

g_h = int(goal[0:2])
g_m = int(goal[3:5])
g_mm = int(goal[6:])

if g_mm < c_mm:
    g_m -= 1
    g_mm += 60
if g_m < c_m:
    g_h -= 1
    g_m += 60
if g_h < c_h:
    g_h += 24

if goal == current:
    print("24:00:00")

else:
    if len(str(g_h-c_h)) == 1:
        ans = "0" + str(g_h-c_h) + ":"
    else:
        ans = str(g_h-c_h) + ":"

    if len(str(g_m-c_m)) == 1:
        ans += "0" + str(g_m-c_m) + ":"
    else:
        ans += str(g_m-c_m) + ":"

    if len(str(g_mm-c_mm)) == 1:
        ans += "0" + str(g_mm-c_mm) 
    else:
        ans += str(g_mm-c_mm)

    print(ans)