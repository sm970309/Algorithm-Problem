# 아이디어
# ex) 5까지 뛰는 경우의 수 -> (3까지 뛴경우 + 2칸 뛰기) + (4까지 뛴 경우 + 1칸 뛰기)
# 즉, 피보나치 수열이라고 생각가능

def solution(n):
    if n <=1:
        return 1
    d=[0]*n
    d[0]=1
    d[1]=2
    for i in range(2,n):
        d[i] = d[i-1]+d[i-2]
    return d[n-1]%1234567