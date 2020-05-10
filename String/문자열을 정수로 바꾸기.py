def solution(s):
    ans = 0
    num_dic = {}

    for i in range(10):
        num_dic[str(i)] = i

    for idx, num in enumerate(s[::-1]):
        if num == '-':
            ans *= -1
        else:
            ans += num_dic[num] * (10 ** idx)

    return ans
