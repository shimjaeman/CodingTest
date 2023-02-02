def solution(triangle):
    sum_list = [[0 for _ in range(i+1)] for i in range(len(triangle))]
    sum_list[0][0] = triangle[0][0]
    for i in range(len(triangle)):
        for j in range(i):
            sum_list[i][j] = max(sum_list[i][j], sum_list[i-1][j] + triangle[i][j])
            sum_list[i][j+1] = sum_list[i-1][j] + triangle[i][j+1]
    return max(sum_list[-1])