def solution(clothes):
    clothes_dict = {}
    for i in range(len(clothes)):
        type = clothes[i][1]
        if type not in clothes_dict:
            clothes_dict[type] = 1
        else:
            clothes_dict[type] += 1
    n = list(clothes_dict.values())
    ans = 1
    for i in range(len(n)):
        ans *= (n[i] + 1)
    return ans - 1