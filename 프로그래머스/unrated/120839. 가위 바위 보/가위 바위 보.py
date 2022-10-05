def solution(rsp):
    result = ""
    for i in rsp :
        if i == "2":
            result += "0"
        elif i == "0":
            result += "5"
        elif i == "5":
            result += "2"
    return result