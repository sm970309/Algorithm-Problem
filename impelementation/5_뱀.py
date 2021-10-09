n = int(input())
k = int(input())
# 전체 판
matrix = [[0]*n for _ in range(n)]
# 뱀의 현재 위치
visited = [[False]*n for _ in range(n)]
visited[0][0] = True
# 뱀의 이동 방향
moves = []
# 이동 경우 (우 하 좌 상) 순서
direction = [(0,1),(1,0),(0,-1),(-1,0)]
# 뱀 길이와 현재 시간
length,sec = 1,0

for _ in range(k):
    row,col = map(int,input().split())
    matrix[row-1][col-1] = 1
print(matrix)

l = int(input())
for _ in range(l):
    # x는 초, c는 방향(L:좌 D:우)
    x,c = input().split()
    moves.append((int(x),c))

# 현재 위치
x,y = 0,0
# 이동 방향
d = 0

for move in moves:
    while sec<=move[0]:
        for _ in range(length):
            nx,ny = x+direction[d][0],y+direction[d][1]
            if nx>=n or ny>=n or nx<0 or ny<0:

                break
            if visited[nx][ny]:

                break

            # 몸길이를 늘려 다음 칸에 위치
            visited[nx][ny]=True

            if matrix[nx][ny]:
                matrix[nx][ny]=0
                length += 1
            else:
                visited[x][y]=False

        if move[0] == sec:
            if move[1]=="L":
                if d==0:
                    d=3
                else:
                    d -=1
            elif move[1]=="D":
                if d==3:
                    d=0
                else: d+=1
        sec+=1
        x,y = nx,ny
        print(visited)
        print()
