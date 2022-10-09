alpha = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
alpha_dict = {"zero" : 0, "one" : 1, "two" : 2, 
              "three" : 3, "four" : 4, "five" : 5, 
              "six" : 6, "seven" : 7, "eight": 8, 
              "nine": 9}

# numbers 각 영어 숫자 분리
def split_num(numbers) :
    answer = []
    check_point = ""
    for num in numbers: 
        check_point += num
        for al in alpha:
            if check_point == al:
                answer.append(al)
                check_point = ""
    return answer


def solution(numbers):
    result = ""
    for num in split_num(numbers):
        result += str(alpha_dict[num])
    return int(result)