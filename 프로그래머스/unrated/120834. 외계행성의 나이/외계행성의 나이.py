age_type = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
def solution(age):
    result =""
    age_str = str(age)
    for p in age_str:
        result += age_type[int(p)]
    return result