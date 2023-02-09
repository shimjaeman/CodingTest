from heapq import heappush, heappop, heapify
def solution(scoville, K):
    new_scov = scoville
    heapify(new_scov)
    new_scov.sort()
    cnt = 0
    while new_scov[0] < K:
            if len(new_scov) == 1:
                return -1
            start_num = heappop(new_scov)
            end_num = heappop(new_scov)
            new_scov_num = start_num + (2 * end_num)
            heappush(new_scov, new_scov_num)
            cnt +=1
    return cnt