# chr() : ASCII값을 문자(Character)로 변환 ex) 97 -> "a"
# ord() : 문자(Character)에 대한 ASCII값을 반환 ex) "a" -> 97

def solution(age):
    return ''.join([chr(ord('a')+int(i)) for i in str(age)])
