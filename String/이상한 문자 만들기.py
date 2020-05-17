def solution(s):
    ans = ''
    idx = 0
    for ele in s:
        if ele.isalpha():
            idx += 1
            if idx % 2:
                ans += ele.upper()
            else:
                ans += ele.lower()
        else:
            idx = 0
            ans += ' '
            continue

    return ans