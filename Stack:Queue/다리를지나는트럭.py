from collections import deque


def solution(bridge_length, weight, truck_weights):
    t = 0
    queue = deque([0] * bridge_length)

    while queue:
        t += 1
        queue.popleft()
        if truck_weights:
            if sum(queue) + truck_weights[0] <= weight:
                queue.append(truck_weights.pop(0))
            else:
                queue.append(0)
    return t