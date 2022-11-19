a = int(input())

score = 0
sum_score = 0

for i in range(a):
    score = 0
    sum_score = 0
    test = list(input())
    for j in test:
      if j == "O":
        score += 1
        sum_score += score
      else : 
        score = 0
    print(sum_score) 