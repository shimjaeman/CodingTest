def solution(emergency):
    result =[]
    answer = {emer : id+1 for id, emer in sorted(enumerate(sorted(emergency, reverse = True)))}
    return [answer[i] for i in emergency]