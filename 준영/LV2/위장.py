# from itertools import combinations

# def solution(clothes):
#     answer = 0
#     dict_name_arr = []
#     dict_arr = []
#     for c in clothes:
#         if c[1] not in dict_name_arr:
#             dict_name_arr.append(c[1])
#             dict_arr.append([c[0]])
#         else:
#             idx = dict_name_arr.index(c[1])
#             dict_arr[idx].append(c[0])
            
#     N = len(dict_name_arr)
#     for n in range(1, N+1):
#         comb_list = combinations(dict_name_arr, n)
#         for comb in comb_list:
#             temp = 1
#             for c in comb:
#                 idx = dict_name_arr.index(c)
#                 temp *= len(dict_arr[idx])
#             answer += temp
#     return answer


def solution(clothes):
    answer = 1
    dict_name_arr = []
    dict_arr = []
    for c in clothes:
        if c[1] not in dict_name_arr:
            dict_name_arr.append(c[1])
            dict_arr.append([c[0]])
        else:
            idx = dict_name_arr.index(c[1])
            dict_arr[idx].append(c[0])
    
    for i in dict_arr:
        answer *= (len(i) + 1)
    answer -= 1
    return answer 

clothes = [["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]
solution(clothes)