def solution(s):
    answer = len(s)

    for step in range(1, len(s) // 2 + 1):
        word = ''
        count = 1
        prev = s[:step]
        tmp = 0
        for i in range(step, len(s) + 1, step):
            if prev == s[i:i + step]:
                count += 1
            else:
                if count > 1:
                    word += str(count) + prev
                    count = 1
                elif count == 1:
                    word += prev
            prev = s[i:i + step]
            if len(prev) != step:
                word += prev
        answer = min(answer, len(word))
    return answer