numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]

hand = "right"

board = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [11, 0, 12]
]

def find_xy(a):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == a:
                return i, j

# print(find_xy(1))

answer = ""
right_now = (3, 2)
left_now = (3, 0)
for i in range(len(numbers)):
    if numbers[i] in [1, 4, 7]:
        answer += "L"
        left_now = find_xy(numbers[i])

    elif numbers[i] in [3, 6, 9]:
        answer += "R"
        right_now = find_xy(numbers[i])

    else:
        n_y, n_x = find_xy(numbers[i])

        if abs(right_now[0]-n_y) + abs(right_now[1]-n_x) > abs(left_now[0]-n_y) + abs(left_now[1]-n_x):
            answer += "L"
            left_now = n_y, n_x
        elif abs(right_now[0]-n_y) + abs(right_now[1]-n_x) < abs(left_now[0]-n_y) + abs(left_now[1]-n_x):
            answer += "R"
            right_now = n_y, n_x

        else:
            if hand == "right":
                answer += "R"
                right_now = n_y, n_x
            else:
                answer += "L"
                left_now = n_y, n_x

print(answer)
