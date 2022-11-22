def solution(score):
    dict = {}
    new_score = [((score[i][0] + score[i][1]) / 2) for i in range(len(score))]
    for k, v in enumerate(sorted(new_score, reverse=True), 1):
        if v not in dict:
            dict[v] = k
    return [dict[i] for i in new_score]