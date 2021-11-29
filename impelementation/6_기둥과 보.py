# a: 기둥0,보1 b: 삭제0 설치1

# possible이란 메소드를 사용하여 제거하거나 추가했을때 가능한 상황인지 판단 후 이상이 없으면 그대로 진행
def possible(answer):
    for x, y, a in answer:
        if a == 1:
            if [x, y - 1, 0] in answer or [x + 1, y - 1, 0] in answer or (
                    [x - 1, y, 1] in answer and [x + 1, y, 1] in answer):
                continue
            return False
        elif a == 0:
            if y == 0 or [x - 1, y, 1] in answer or [x, y, 1] in answer or [x, y - 1, 0] in answer:
                continue
            return False
    return True


def solution(n, build_frame):
    answer = []
    for build in build_frame:
        x, y, a, b = build
        if b:
            answer.append([x, y, a])
            if not possible(answer):
                answer.remove([x, y, a])
        else:
            answer.remove([x, y, a])
            if not possible(answer):
                answer.append([x, y, a])
    return sorted(answer)