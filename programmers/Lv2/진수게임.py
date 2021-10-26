def solution(n, t, m, p):
    # n진수에 맞게 num_list 생성
    num_list = (list(map(str,range(10)))+["A","B","C","D","E","F"])[:n]
    # 0부터 n-1까지는 미리 word로 만들어놓음
    word = ''.join(num_list)
    # n부터 최대 t*m 개까지 생성 될 수 있으므로
    for i in range(n,t*m+1):
        tmp = ''    # n진수로 변환한 값을 집어넣을 임시 변수
        num = i
        while num//n>0:
            tmp += num_list[num%n]  #나머지 index에 해당하는 값을 tmp에 추가 (A~F까지도 적용하기 위해)
            num //= n
        tmp += num_list[num%n]
        word += tmp[::-1]
    answer = ''.join([word[i] for i in range(p-1,t*m,m)])   # p-1번째부터 m간격으로 t*m까지 join
    return answer