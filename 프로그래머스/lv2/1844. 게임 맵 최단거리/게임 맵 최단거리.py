from collections import deque

def solution(maps):
    # 기본값 설정
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    nx, ny = len(maps), len(maps[0])
    
    # deque 설정
    que = deque()
    start = (0,0)
    que.append(start)
    
    while que:
        x,y = que.popleft()
        
        for i in range(4):
            new_dx = x + dx[i]
            new_dy = y + dy[i]
                            
            if 0 <= new_dx < nx and 0 <= new_dy < ny and maps[new_dx][new_dy] == 1:
                maps[new_dx][new_dy] = maps[x][y] + 1 # 값 누적
                que.append((new_dx,new_dy))

    return maps[nx-1][ny-1] if maps[nx-1][ny-1] > 1 else -1
        