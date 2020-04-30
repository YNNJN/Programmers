#mid값으로 접근하기보단 정렬을 잘 이용해보자

def solution(citations):
    citations.sort()
    l = len(citations)
    for i in range(l):
        if citations[i] >= l-i:
            return l-i
    return 0