def solution(s) :
    answer = s[2:-2].split("},{")
    result = []
    for i in answer:
        result.append(i.split(","))
    sort_result = sorted(result, key = lambda x : len(x))
    
    test = []
    for i in sort_result:
        for j in range(len(i)):
            if int(i[j]) not in test:
                test.append(int(i[j]))
                break
    return test