# 블로그 참조
# 아이디어 -> dp를 사용하여 해결, 정사각형의 길이를 중첩해 나가는 방식

def solution(board):
    maxv = 0
    for x in range(len(board)):
        for y in range(len(board[0])):
            # 범위를 벗어나면 continue
            if x-1<0 or y-1<0:
                continue
            # 현재 값이 0이면 continue(0이므로 정사각형이 이어질 수가 없음)
            if board[x][y] == 0:
                continue
            board[x][y] = min(board[x-1][y-1],board[x-1][y],board[x][y-1])+1
    for val in board:
        maxv = max(maxv,max(val))
    return maxv**2