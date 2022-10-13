# zip() : zip(*iterable)은 동일한 개수로 이루어진 자료형을 묶어 주는 역할을 하는 함수
# for x, y in zip(a,b)와 같이 a,b의 각 리스트의 값을 x, y에 넣는게 가능하다.
def getMinSum(A,B):
    return sum(a*b for a, b in zip(sorted(A), sorted(B, reverse = True)))
