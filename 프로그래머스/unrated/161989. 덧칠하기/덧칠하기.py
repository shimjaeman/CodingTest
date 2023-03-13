def solution(n, m, section):
    paint, answer = section[0]-1, 0
    while section:
        if paint < section[0] :
            paint = section[0] + m - 1
            answer += 1
        del section[0]
    return answer