from itertools import chain

def solution(n):
    graph = [[0] * n for _ in range(n)]
    y, x = -1, 0
    num = 1
    for i in range(n):
        for _ in range(i, n):
            if i % 3 == 0:
                y += 1
            elif i % 3 == 1:
                x += 1
            elif i % 3 == 2:
                y -= 1
                x -= 1
            graph[y][x] = num
            num += 1
    ans = [i for i in chain(*graph) if i != 0]
    return ans