# 모음 리스트를 만들어 반복문을 사용하여 모음에 해당하는 문자를 replace를 사용하여 ""로 바꿔준다.

def solution(my_string):
    vowels = ['a','e','i','o','u']
    for vowel in vowels:
        my_string = my_string.replace(vowel, '') 
    return my_string
    
