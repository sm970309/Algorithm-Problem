# 주요 아이디어 -> 완전 탐색 문제임을 인지
# 모든 경우를 구해보기 위해 자물쇠 크기의 3배크기인 새로운 행렬을 생성
# 행렬의 가운데에 자물쇠 놓고 열쇠를 처음부터 끝까지 옮겨가며 대입해봄

def solution(key, lock):
    m = len(key)
    n = len(lock)

    new_matrix = [[0] * (n * 3) for _ in range(n * 3)]
    for i in range(n):
        for j in range(n):
            new_matrix[i + n][j + n] = lock[i][j]

    for _ in range(4):
        key = turn(key)

        for x in range(1, n * 2):
            for y in range(1, n * 2):
                for i in range(m):
                    for j in range(m):
                        new_matrix[x + i][y + j] += key[i][j]
                if check(new_matrix):
                    return True
                for i in range(m):
                    for j in range(m):
                        new_matrix[x + i][y + j] -= key[i][j]
    return False

# 90도 회전시켜주는 함수
def turn(matrix):
    new_matrix = []
    for i in range(len(matrix)):
        temp = []
        for row in matrix:
            temp.append(row[i])
        new_matrix.append(list(reversed(temp)))
    return new_matrix

def check(matrix):
    length = len(matrix) // 3
    for i in range(length, length * 2):
        for j in range(length, length * 2):
            if matrix[i][j] != 1:
                return False
    return True