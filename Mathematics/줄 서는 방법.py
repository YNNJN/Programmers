'''
첫번째 숫자는 n!/n번 나옴
이후 k는 1부터 시작하므로 첫번째 숫자의 배열 인덱스는 (k-1)/(n!/n) -> (k-1)/(n-1)!
첫번째를 구한 후 k = (k-1) % (n-1)!

'''

import math

def solution(n,k):
    nums = list(range(1, n+1))
    ans = []
    while n:
        n -= 1
        p,r = divmod(k, math.factorial(n))
        if r == 0:
            p -= 1
        ans.append(nums[p])
        nums.remove(nums[p])
        k = r
    return ans

#print(solution(3,5))