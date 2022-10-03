def solution(array, height):
    cnt = [i for i in array if i > height]
    return len(cnt)