def solution(X, Y):
    # 공통으로 나타나는 정수를 이용하여 만들 수 있는 가장 큰 정수
    par_list = []
    for i in range(10):
        if X.count(str(i)) != 0 and Y.count(str(i)) != 0:
            add_num = [str(i)] * min(X.count(str(i)), Y.count(str(i)))
            par_list.extend(add_num)
    
    # X, Y의 짝꿍이 존재하지 않으면, -1
    if par_list == []:
        return "-1"
    
    # X, Y의 짝꿍이 0으로만 구성, 0
    if list(set(par_list)) == ["0"]:
        return "0"
    
    result = "".join(sorted(par_list)[::-1])      
    return result