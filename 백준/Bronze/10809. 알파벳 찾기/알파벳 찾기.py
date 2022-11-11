alpha = [i for i in "abcdefghijklmnopqrstuvwxyz"]
N = input()
for i in range(len(alpha)):
    if alpha[i] in N:
        print(N.index(alpha[i]))
    else :
        print(-1)