def solution(absolutes, signs):
    return  sum(absolute if sign else -absolute for absolute, sign in zip(absolutes, signs))
    
# zip()함수 : zip() 함수는 여러 개의 순회 가능한(iterable) 객체를 인자로 받고, 
#             각 객체가 담고 있는 원소를 터플의 형태로 차례로 접근할 수 있는 반복자(iterator)를 반환
# numbers = [1, 2, 3]
# letters = ["A", "B", "C"]
# for pair in zip(numbers, letters):
#     print(pair)
# (1, 'A')
# (2, 'B')
# (3, 'C')
