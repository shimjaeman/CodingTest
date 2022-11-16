from collections import deque
def solution(cacheSize, cities):
    answer = [""] * cacheSize 
    cash = deque(answer, maxlen = cacheSize)
    cnt = 0
    for city in cities:
        city = city.lower()
        if city in cash:
            cash.remove(city)
            cash.append(city)
            cnt +=1
        else :
            cash.append(city)
            cnt +=5
    return cnt