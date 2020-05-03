def solution(tickets):
    t = {}
    for ticket in tickets:
        if ticket[0] in t:
            t[ticket[0]].append(ticket[1])
        else:
            t[ticket[0]] = [ticket[1]]
    for k in t.keys():
        t[k].sort(reverse=True) #도착지를 역순으로 저장

    s = ['ICN']
    ans = []

    while s:
        top = s[-1]
        if top not in t or len(t[top]) == 0: #출발지에 없거나 도착지를 다 돌았으면
            ans.append(s.pop())
        else:
            s.append(t[top][-1])
            t[top].pop()

    return ans[::-1] #스택이면 거꾸로 들어가므로