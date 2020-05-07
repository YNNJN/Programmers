# def solution(number, k):
#     stack = [number[0]]
#     for num in number[1:]:
#         while len(stack) > 0 and stack[-1] < num and k > 0:
#             k -= 1
#             stack.pop()
#         stack.append(num)
#     if k != 0: #제거 횟수 다 사용하지 않았을 때
#         stack = stack[:-k] #남은 횟수만큼 리스트 뒷부분을 슬라이싱
#     return ''.join(stack)


def solution(number, k):
    stack = []
    for i in range(len(number)):
        while stack and k > 0 and stack[-1] < number[i]:
            stack.pop()
            k -= 1
        stack.append(number[i])
    return ''.join(stack[:len(stack) - k])