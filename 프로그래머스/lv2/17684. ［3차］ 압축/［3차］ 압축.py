from collections import Counter
def solution(msg):
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    alpha_dict = { j : i+1 for i, j in enumerate(alpha)}
    len_msg = len(msg)
    i, index_num = 0, 27
    answer = []
    while len_msg > i:
        temp = ""
        for n in range(i, len_msg):
            temp += msg[n]
            if temp not in list(alpha_dict.keys()):
                answer.append(alpha_dict[temp[:-1]])
                i = n
                alpha_dict[temp] = index_num
                index_num +=1
                break
        else :
            answer.append(alpha_dict[msg[i:]])
            break
    return answer