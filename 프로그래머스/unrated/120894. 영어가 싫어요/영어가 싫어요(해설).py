# enumerate() : 목록을 인덱스와 원소로 이루어진 터플(tuple)을 만들어줍니다. 
def solution(numbers):
    for num, eng in enumerate(["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]):
        numbers = numbers.replace(eng, str(num)) # 각 숫자영어를 str(num) 즉 인덱스로 replace 시킨다
    return int(numbers) # 최종적으로 int로 변경
