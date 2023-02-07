def solution(word):
    alphabet = ['A', 'E', 'I', 'O', 'U']
    global answer
    answer = 0
    def dfs (alpha):
        global answer
        answer += 1
        if alpha == word:
            return True
        
        if len(alpha) == 5:
            return False
        
        for a in alphabet:
            if dfs(alpha + a) :
                return True
    for a in alphabet:
        if dfs(a):
            return answer