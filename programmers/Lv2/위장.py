# 시간 초과 코드, combination을 사용하여 각각의 경우의 수 계산한게 시간초과 원인인듯

from itertools import combinations
def solution(clothes):
    answer = 0
    d = {}
    for cloth in clothes:
        d[cloth[1]] = 0
    for cloth in clothes:
        d[cloth[1]] += 1
    cloth = list(d.values())
    for i in range(1, len(d) + 1):
        tmp = list(combinations(cloth, i))
        for x in tmp:
            n = 1
            for y in x:
                n *= y
            answer += n

    return answer

# 참조 코드
def solution(clothes):
    answer = 1
    d = {}
    for cloth in clothes:
        d[cloth[1]] = 0
    for cloth in clothes:
        d[cloth[1]] += 1
    # val+1을 해주는 이유는, 착용하지 않은 경우도 세어주기 위함
    for val in d.values():
        answer *= (val + 1)

    # 모두 착용 안한 경우는 빼야 하므로 -1
    return answer - 1