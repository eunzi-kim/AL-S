import sys

data = sys.stdin.read()
tree = data.split('\n')

tree_dict = {}

total = 0

for i in tree:
    if i == '':
        continue
    total += 1
    if tree_dict.get(i):
        tree_dict[i] += 1
    else:
        tree_dict[i] = 1

trees = list(tree_dict.keys())
trees.sort()

for key in trees:
    print("%s %.4f" % (key, tree_dict[key]/total*100))