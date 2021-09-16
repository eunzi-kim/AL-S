N = int(input())

my_dict = {}
arr = [[0] * 2 for _ in range(26)]
for i in range(26):
    my_dict[chr(ord('A')+i)] = i

for _ in range(N):
   p, l, r = input().split()
   arr[my_dict[p]][0] = l
   arr[my_dict[p]][1] = r

def preorder(a):
    print(a, end="")
    if arr[my_dict[a]][0] != ".":
        preorder(arr[my_dict[a]][0])
    if arr[my_dict[a]][1] != ".":
        preorder(arr[my_dict[a]][1])

def inorder(a):
    if arr[my_dict[a]][0] != ".":
        inorder(arr[my_dict[a]][0])
    print(a, end="")
    if arr[my_dict[a]][1] != ".":
        inorder(arr[my_dict[a]][1])

def postorder(a):
    if arr[my_dict[a]][0] != ".":
        postorder(arr[my_dict[a]][0])
    if arr[my_dict[a]][1] != ".":
        postorder(arr[my_dict[a]][1])
    print(a, end="")


preorder("A")
print()
inorder("A")
print()
postorder("A")