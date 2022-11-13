


# def solution(a, b):
#     a_list = a
#     b_list = [l for l in b]
#     result_list = []
#     n = 0
#     trigger = False
#     for index, letter in enumerate(b_list):
#         if letter in a_list:
#             if not trigger:
#                 result_list.append([])
#                 trigger = True

#             result_list[n].append(b_list.pop(index))

#         try:
#             if len(result_list[n]) == len(a):
#                 trigger = False
#                 n += 1
#         except:
#             pass        
        
#     return n + 1

