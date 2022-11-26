def solution(phone_book):
    answer = sorted(phone_book)
    ans_len = len(answer)
    for i in range(ans_len-1):
        if answer[i] == (answer[i+1])[:len(answer[i])]:
            return False
    return True
