from collections import Counter

n = int(input())
cards = list(map(int, input().split()))
m = int(input())
checks = list(map(int, input().split()))

# 각 숫자 카드의 개수를 세어줌
counter = Counter(cards)

# 각 숫자 카드가 몇 개 있는지 출력
for check in checks:
    print(counter[check], end=' ')