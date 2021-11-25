# (이전x좌표,이전y좌표,x좌표,y좌표) 형태로 stack에 저장
# 동일한 경로가 있으면 카운트 생략

def solution(dirs):
    answer = 0
    x,y = 0,0
    stack = []
    direct = ["U","D","R","L"]
    move = [(0,1),(0,-1),(1,0),(-1,0)]
    for d in dirs:
        dx,dy = move[direct.index(d)]
        # 범위를 벗어나면 카운트 생략
        if not -5<=x+dx<=5:
            continue
        if not -5<=y+dy<=5:
            continue
        x += dx
        y += dy
        if (x-dx,y-dy,x,y) in stack or (x,y,x-dx,y-dy) in stack:
            continue
        stack.append((x-dx,y-dy,x,y))
        answer += 1
    return answer