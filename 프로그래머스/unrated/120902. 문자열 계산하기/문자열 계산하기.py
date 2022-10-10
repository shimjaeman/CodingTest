def solution(my_string):
    str_split = my_string.split(" ")
    tot = int(str_split[0])
    for i in range(len(str_split)):
        if str_split[i] == "+":
            tot += int(str_split[i+1])
            
        elif str_split[i] == "-":
            tot -= int(str_split[i+1])
        
    return tot