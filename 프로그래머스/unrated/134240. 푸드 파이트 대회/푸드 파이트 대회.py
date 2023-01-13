def solution(food):
    # 음식의 배치를 짝수로 배분
    new_food = []
    for i, j in enumerate(food) :
        if j % 2 == 0:
            new_food.append((i, j // 2))
        else :
            new_food.append((i, (j-1) // 2))
    
    # 배분한 결과를 가지고 음식 배치
    result = ""
    for i in range(len(new_food)):
        if new_food[i][1] == 0:
            continue
        else :
            result += str(new_food[i][0]) * new_food[i][1]
        
        
        
    
    return result + "0" + result[::-1]