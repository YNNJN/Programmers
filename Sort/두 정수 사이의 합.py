def solution(a, b):
    if a > b: a, b = b, a
    interval = range(a, b+1)
    return sum(interval)