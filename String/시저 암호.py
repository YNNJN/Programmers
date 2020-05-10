def solution(s, n):
    ans = ''
    for ele in s:
        if ele.isalpha():
            if ele.islower():
                ans += chr((ord(ele) - ord('a') + n) % 26 + ord('a'))
            else:
                ans += chr((ord(ele) - ord('A') + n) % 26 + ord('A'))
        else:
            ans += ' '

    return ans