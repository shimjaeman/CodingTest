import re
def solution(files):
    my_files = []
    answer = []
    for i, idx in enumerate(files):
        number = re.findall("\d+", idx)[0]
        head = idx[:idx.index(number)]
        number = int(number)
        head = head.lower()
        my_files.append([head, number, i])
        my_files.sort(key=lambda x : (x[0], x[1]))
        answer = [files[n[2]] for n in my_files]
    return answer