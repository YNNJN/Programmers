#M1 인쇄 목록과 인덱스를 함께 기억 -> enumerate()
#M2 어차피 인쇄되는 건 우선순위가 가장 큰 값이니, 해당 값을 기준으로 조건을 분기

def solution(priorities, location):
    ans = 0
    m = max(priorities)
    while True:
        v = priorities.pop(0)
        if m == v:
            ans += 1
            if location == 0:
                break
            else:
                location -= 1
            m = max(priorities)
        else:
            priorities.append(v)
            if location == 0:
                location = len(priorities) - 1
            else:
                location -= 1
    return ans
