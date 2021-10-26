# eval의 사용법 -> 문자열 그 자체를 연산

from itertools import permutations
def solution(expression):
    answer = 0
    simbol = []

    # 해당 expression에서 사용되는 기호에 따라 순열 생성
    if "-" in expression:
        simbol.append("-")
    if "*" in expression:
        simbol.append("*")
    if "+" in expression:
        simbol.append("+")

    # 기호가 들어간 순열 리스트
    orders = list(permutations(simbol))

    # 길이가 1이다 -> 기호가 하나밖에 쓰이지 않았다
    if len(orders) == 1:
        # 그 자체로 계산 가능하여 바로 return
        return abs(eval(expression))

    # 우선 순위에 따라 리스트를 나눠줌
    for order in orders:
        first = order[-1]   # 마지막 우선순위
        second = order[-2]  # 그 다음 우선순위

        # 우선순위가 낮은 것부터 나눠줘야 우선순위가 높은 연산자부터 계산 가능
        n = expression.split(first) # 처음 나눠진 리스트(가장 낮은 연산자 기준)
        nn = []    # 두 번째 나눠진 리스트(그 다음 연산자 기준)
        for new in n:
            nn.append(new.split(second))
        nnn = []    # 세 번째 나눠진 리스트(가장 우선순위가 높은 리스트)
        for x in nn:
            temp = []
            for y in x:
                # y 에는 '3*2' 이런 식의 값이 들어가 있기 때문에 eval로 바로 계산
                temp.append(eval(y))
            nnn.append(temp)
        nnnn = []       # 나눠진 리스트를 합쳐주는 과정(두번째 우선순위)
        for x in nnn:
            if len(x) == 1:     # 값이 하나, 즉 연산이 필요없으면 그대로 append
                nnnn.append(x[0])
            else:
                temp = list(map(str, x))
                nnnn.append(eval(second.join(temp)))    # second 연산자와 join 후 eval로 값 게산

        nnnnn = list(map(str, nnnn))    # 나눠진 리스트를 합쳐주는 과정(첫번째 우선순위)
        answer = max(answer, abs(eval(first.join(nnnnn))))  # first 연산자와 join 후 eval로 값 계산

    return answer