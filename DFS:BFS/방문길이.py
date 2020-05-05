def solution(dirs):
    dr, dc = [-1, 0, 1, 0], [0, -1, 0, 1]
    d = {'U': 0, 'L': 1, 'D': 2, 'R': 3}

    visited = set()
    answer = 0
    r, c = 0, 0
    for dir in dirs:
        i = d[dir]
        nr, nc = r + dr[i], c + dc[i]
        if nr < -5 or nr > 5 or nc < -5 or nc > 5:
            continue
        if (r, c, nr, nc) not in visited:
            visited.add((r, c, nr, nc))  # 한 번 가본 길 저장
            visited.add((nr, nc, r, c))  # 반대 경우도 함께 저장
            answer += 1
        r, c = nr, nc

    return answer