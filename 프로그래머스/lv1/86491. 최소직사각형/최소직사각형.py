def solution(sizes):
    answer = []
    width = 0
    height = 0
    for i in range(len(sizes)):
        answer.append(sizes[i].sort())
    
    for i in range(len(sizes)):
        if width < sizes[i][0]:
            width = sizes[i][0]
    
    for i in range(len(sizes)):
        if height < sizes[i][1]:
            height = sizes[i][1]
    return width * height