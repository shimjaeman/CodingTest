def solution(n, words):    
    p = [words[0]]
    print(p)
    for i, j in enumerate(words[1:], 1):
        if j not in p and p[-1][-1] == j[0]:
            p.append(j)
        else :
            return [i % n + 1, (i//n)+1]
    return [0,0]