import math


def solution(n, stations, w):
    ans = 0
    start = 0
    for i in range(len(stations)):
        left = stations[i] - w - 1
        right = stations[i] + w - 1
        if start >= left and start <= right:
            start = right + 1
            continue
        ans += math.ceil((left - start) / (w * 2 + 1))
        start = right + 1
    if start < n:
        ans += math.ceil((n - start) / (w * 2 + 1))
    return ans
