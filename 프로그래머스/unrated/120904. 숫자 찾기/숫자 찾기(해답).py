# 풀이방법(1)
# find를 사용
# 찾은 경우 [찾은위치+1] / 찾지 못한 경우 [-1+1]
# answer == 0(찾지못한경우) -> return -1
def solution (num, k):
  answer = (str(num).find(str(k)))+1
  if answer == 0 :
    return -1
  return answer

# 풀이방법(2)
# index를 사용
# try / except를 사용하여 예외의 상항이 나오는 index를 사용
def solution (num, k):
  try:
    return str(num).index(str(k)) + 1
  except ValueEroor:
    return -1
