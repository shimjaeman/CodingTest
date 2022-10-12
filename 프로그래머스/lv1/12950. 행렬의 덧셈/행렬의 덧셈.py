def solution(arr1, arr2):
    result = []
    for i in range(len(arr1)):
        result.append([])
        for j in range(len(arr1[i])):
            result[i].append(arr1[i][j] + arr2[i][j])
    return result