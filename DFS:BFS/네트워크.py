def solution(n, computers):
    ans = 0
    queue = []
    visited = [0] * n

    while 0 in visited:
        x = visited.index(0)
        queue.append(x)
        visited[x] = 1

        while queue:
            node = queue.pop(0)
            visited[node] = 1
            for i in range(n):
                if visited[i] == 0 and computers[node][i] == 1: #인접노드이고 방문하지 않은 경우
                    queue.append(i)
                    visited[i] = 1
        ans += 1
    return ans

