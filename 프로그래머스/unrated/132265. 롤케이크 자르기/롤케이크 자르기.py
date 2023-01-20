from collections import Counter, defaultdict
def solution(topping):
    result = 0
    total = Counter(topping)
    end_dict = defaultdict(object)
    end_dict = defaultdict(lambda : 0)
    
    while len(topping) > 1 :
        value = topping.pop()
        end_dict[value] += 1
        if total[value] > 1:
            total[value] = total[value] - 1
        else :
            del total[value]
        
        if len(total) == len(end_dict):
            result += 1
        
    return result