# 남이 풀어놓은 풀이 참조한 코드
# 아이디어만 보고 코딩은 직접함
# 해당 리스트 값에 전 리스트 값의 최대값을 더해주는 식으로 진행
# 만약 최대값의 인덱스와 현재 인덱스가 같으면, 두번째로 큰 값을 더해주는 식으로 진행

def solution(land):
    for i in range(1,len(land)):
        max_idx = land[i-1].index(max(land[i-1]))
        second = sorted(land[i-1])
        s_max = second[-2]
        for j in range(4):
            if j==max_idx:
                land[i][j] += s_max
            else:
                land[i][j] += max(land[i-1])

    return max(land[-1])