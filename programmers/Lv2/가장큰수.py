# 아이디어(떠올리긴 했지만, 구현 못함)
# 한자리 or 두자리인 수를 정렬하기 위해 *3을 해주어 최소 3자리를 만들어준다

# 프로그래머스 방식
def solution1(numbers):
    numbers = list(map(str, numbers))
    # lambda를 사용하여 정렬 -> x*3형식
    numbers.sort(key=lambda x: x*3, reverse=True)
    return str(int(''.join(numbers)))

# 인터넷 참고 방식
def solution2(numbers):
    answer = ''
    numbers2= [str(n)*3 for n in numbers]
    numbers3 = list(enumerate(numbers2))
    numbers3 = sorted(numbers3,key=lambda x:x[1],reverse = True)
    for idx,num in numbers3:
        answer+=str(numbers[idx])
    return str(int(answer))