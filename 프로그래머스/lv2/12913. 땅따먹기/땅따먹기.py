# 열의 개수는 4개이고, 땅(land)은 2차원 배열로 주어집니다.
def solution(land):
    for la in range(1, len(land)):
        land[la][0] += max(land[la-1][1], land[la-1][2], land[la-1][3])
        land[la][1] += max(land[la-1][2], land[la-1][3], land[la-1][0])
        land[la][2] += max(land[la-1][3], land[la-1][0], land[la-1][1])
        land[la][3] += max(land[la-1][0], land[la-1][1], land[la-1][2])
    return max(land[-1])