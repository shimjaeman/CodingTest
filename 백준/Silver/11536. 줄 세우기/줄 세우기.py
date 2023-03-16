n = int(input())
words = []

for i in range(n):
    word = input()
    words.append(word)

sorted_words = sorted(words)

if words == sorted_words:
    print("INCREASING")
elif words == sorted_words[::-1]:
    print("DECREASING")
else:
    print("NEITHER")