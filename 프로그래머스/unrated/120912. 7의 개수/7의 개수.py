def solution(array):
    answer = ""
    for i in range(len(array)):
        answer += str(array[i])
    return answer.count("7")