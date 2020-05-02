# #정확성 테스트 통과, 효율성 테스트 통과 x
# #정렬 알고리즘 시간복잡도는 O(nlog(n))
# #따라서 이 코드 전체의 시간복잡도는 O(n*nlog(n))
# def solution(scoville, K):
#     cnt = 0
#     while min(scoville) < K:
#         scoville.sort()
#         try:
#             scoville.append(scoville.pop(0) + 2*scoville.pop(0))
#         except IndexError:
#             return -1
#         cnt += 1
#     return cnt

#heapq - 리스트의 요소를 push, pop 할 때마다 자동으로 sort
#힙의 저장과 삭제 연산의 시간 복잡도는 O(log(n))

import heapq as hq

def solution(scoville, K):
    heap = []
    for num in scoville:
        hq.heappush(heap, num)
    cnt = 0
    while heap[0] < K:
        try:
            hq.heappush(heap, hq.heappop(heap) + 2*hq.heappop(heap))
        except IndexError:
            return -1
        cnt += 1
    return cnt