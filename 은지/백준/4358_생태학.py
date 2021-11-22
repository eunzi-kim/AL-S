import sys
input = sys.stdin.readline

all_num = 0
tree_info = {}

while True:
    tree = input().rstrip()
    if tree == "":
        break
    
    if tree not in tree_info:
        tree_info[tree] = 1
    else:
        tree_info[tree] += 1
    all_num += 1

tree_list = sorted(tree_info)

for x in tree_list:
    ans = round((tree_info[x] / all_num) * 100, 4)
    print(x, '%.4f' %ans)