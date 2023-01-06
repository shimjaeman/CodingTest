def solution(t, p):
    result = [t[i:len(p)+i] for i in range(len(t)-len(p)+1)]
    cnt = 0
    for i in result:
      if int(i) <= int(p):
        cnt +=1
    return cnt