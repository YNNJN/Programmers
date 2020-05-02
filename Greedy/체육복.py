# def solution(n, lost, reserve):
#     clothes = [1 for _ in range(n+1)]
#
#     for person in lost:
#         clothes[person-1] -= 1
#
#     for person in reserve:
#         clothes[person-1] += 1
#
#     for i in range(len(clothes)-1):
#         if clothes[i] == 2 and clothes[i - 1] == 0:
#             clothes[i], clothes[i - 1] = 1, 1
#             continue
#         elif clothes[i] == 2 and clothes[i + 1] == 0:
#             clothes[i], clothes[i + 1] = 1, 1
#
#     answer = n - clothes.count(0)
#     return answer

def solution(n, lost, reserve):
    lost_set = set(lost) - set(reserve)
    reserve_set = set(reserve) - set(lost)

    for i in reserve_set:
        if i-1 in lost_set:
            lost_set.remove(i-1)
        elif i+1 in lost_set:
            lost_set.remove(i+1)

    return n - len(lost_set)