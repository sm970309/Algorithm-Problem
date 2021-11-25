# 짝수일때는 무조건 +1만해주면 1개비트 차이만 난다
# 홀수일때는 뒤에서부터 첫번째 0이 언제 나오는지에 따라 그 다음 값이 결정된다
# ex) 101이면 첫번째 0이 나오기 전까지 1이 하나 이므로, 2개이하로 같은 비트는 2^(1-1)번째, 즉 1 큰 값이다.
# ex) 1011이면 첫번째 0이 나오기 전까지 1이 두개 이므로, 2개이하로 같은 비트는 2^(2-1)번째, 즉 2 큰 값이다.
def solution(numbers):
    answer = []
    for number in numbers:
        i = 0
        num = bin(number)
        if number % 2 == 0:
            answer.append(number + 1)
            continue
        for n in reversed(num):
            if n == "1":
                i += 1
            else:
                break
        answer.append(number + 2 ** (i-1))

    return answer