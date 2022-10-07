def solution(cipher, code):
    return "".join([cipher[p] for p in range(code-1,len(cipher),code)])