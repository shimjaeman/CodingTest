def solution(my_string):
    result = []
    for string in my_string :
        if string.islower() == True:
            string = string.upper()
            result.append(string)
        elif string.isupper() == True:
            string = string.lower()
            result.append(string)
    return "".join(result)
        
