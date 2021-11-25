# 이전에 못풀었던 문제 -> 구글 참고해서 해결
# BFS를 활용하여 모든 경우의수 계산
# leaves = [0]으로 시작 -> 처음 실행하면 [1,-1] 그 다음은 [2,0,0,-1] ... 이런식으로 진행
# 경우의 수가 2의 n승 개 만큼 생성

def solution(numbers, target):
    answer = 0
    leaves = [0]
    for number in numbers:
        tmp = []
        for parent in leaves:
            tmp.append(parent + number) # 해당 수를 더하는 경우
            tmp.append(parent - number) # 해당 수를 빼는 경우
        leaves = tmp
    for leave in leaves:
        if leave == target:
            answer += 1

    return answer