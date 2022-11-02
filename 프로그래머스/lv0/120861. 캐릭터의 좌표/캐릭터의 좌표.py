def solution(keyinput, board):
    x, y = 0, 0
    dx = [1, -1]
    dy = [1, -1]
    x_mid, y_mid = (board[0] // 2), (board[1] // 2)
    for key in keyinput:
            if key == "left" and x > -x_mid: 
                x += dx[1]
            elif key == "right" and x < x_mid: 
                x += dx[0]
            elif key == "down" and y > -y_mid: 
                y += dy[1]
            elif key == "up" and y < y_mid: 
                y += dy[0]
    return [x, y]