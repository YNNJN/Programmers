# def solution(arr, divisor):
#     answer = []
#     for i in arr:
#         if i % divisor == 0:
#             answer.append(i)
#     answer.sort()
#     if len(answer) == 0:
#         answer = [-1]
#
#     return answer

#list comprehension
def solution(arr, divisor):
    array = [x for x in arr if x % divisor == 0]
    array.sort()
    return array if len(array) else [-1]