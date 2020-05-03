def solution(n, edge):
    graph = [[] for _ in range(n)]
    dist = [0 for _ in range(n)]
    visited = [0] * (n+1)

    queue = [0]
    visited[0] = 1

    for (a,b) in edge:
        graph[a - 1].append(b - 1)
        graph[b - 1].append(a - 1)

    while queue:
        i = queue.pop(0)
        for j in graph[i]:
            if visited[j] == 0:
                visited[j] = 1
                queue.append(j)
                dist[j] = dist[i] + 1

    ans = dist.count(max(dist))
    return ans