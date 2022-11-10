def solution(s):
    cnt, zero = 0, 0
    while True :
        if s == "1":
            return [cnt, zero]
        cnt +=1
        zero += s.count("0")
        s = bin(s.count("1"))[2:]
        