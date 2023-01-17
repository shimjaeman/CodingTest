from collections import deque
def solution(board, moves):
    # 격자의 가장 아래 칸부터 차곡차곡 쌓여있음
    # 집어 올린 인형은 옆 바구니의 가장 아래 칸부터 순서대로 쌓임
    # 같은 모양의 인형 두 개가 연속해서 쌓이게 되면 2개의 인형 사라짐 (cnt +=1)
    # 만약 인형이 없는 곳에서 크레인을 작동시키는 경우 아무일도 없음
    # 크레인을 모두 작동시킨 후 터트려져 사라진 인형의 개수를 return 
    moves = deque(moves)
    double_cnt = 0
    box_row = 0
    box = []
    # 크레인을 이용하여 box에 담기
    while moves:
        # moves 작동 - 1
        v = moves[0] - 1
        if box_row >= len(board):
            moves.popleft()
            box_row = 0
        if board[box_row][v] != 0:
            box.append(board[box_row][v])
            board[box_row][v] = 0
            moves.popleft()
            box_row = 0
        else :
            box_row +=1
    # 겹치는 숫자의 수 카운트
    i = 1
    while True :
        if box[i-1] == box[i]:
            double_cnt += 2
            box.pop(i)
            box.pop(i-1)
            i = 1
        else :
            i += 1
        if i >= len(box):
            break
            
    return double_cnt