def solution(arr1, arr2):
    a, b = len(arr1), len(arr2[0])
    answer = [[0 for _ in range(b)] for _ in range(a)]
    for k1, v1 in enumerate(arr1):
        for k2, v2 in enumerate(v1):
            for k3 in range(b):
                answer[k1][k3] += arr1[k1][k2] * arr2[k2][k3]
    return answer