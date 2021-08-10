# from itertools import combinations
# def solution(number, k):
#     answer = ''
#     arr = list(number)
#     comb_list = combinations(arr, len(arr)-k)
#     max_val = 0
#     for i in comb_list:
#         temp = int(''.join(i))
#         if max_val < temp:
#             max_val = temp
#     answer = str(max_val)
#     return answer

# def solution(number, k):
#     answer = ''
#     temp = number
#     for i in range(k):
#         temp2 = temp[1:]
#         for j in range(len(temp)):
#             temp3 = temp[:i] + temp[i+1:]
#             if int(temp3) > int(temp2):
#                 temp2 = temp3 
#         temp = temp2
#     answer = temp
#     return answer

def solution(number, k):
    answer = ''
    return answer

number = "1924"
k = 2
solution(number, k)