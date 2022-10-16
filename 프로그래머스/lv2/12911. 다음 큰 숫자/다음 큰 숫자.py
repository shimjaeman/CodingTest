def solution(n):
    a = format(n, "b")
    while True :
        n += 1
        b = format(n, "b")
        if a.count("1") == b.count("1"):
            break
    return n