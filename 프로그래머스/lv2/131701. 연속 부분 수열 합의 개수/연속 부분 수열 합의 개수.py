from collections import Counter
def solution(elements):
    new_elements = 2 * elements
    answer = []
    for i in range(1, len(elements)+1):
        answer.extend(list(set([sum(new_elements[n:n+i]) for n in range(len(elements))])))
    return len(set(answer))