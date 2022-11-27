def solution(id_pw, db):
    answer = ""
    for i in db:
        if i[0] == id_pw[0]:
            if i[1] == id_pw[1]:
               return "login"  
            else :
                return "wrong pw"
        else :
            continue
    return "fail"