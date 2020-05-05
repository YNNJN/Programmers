def solution(budgets, M):
    l, r = 0, max(budgets)
    answer = 0
    while r >= l:
        mid = (l + r)//2
        temp = [i if i < mid else mid for i in budgets]
        if sum(temp) > M:
            r = mid - 1
        else:
            answer = mid
            l = mid + 1
    return answer