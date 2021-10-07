n = int(input())
s = list(map(int,input().split()))
s.sort()

target = 1

for i in s:
    if target >= i:
        target += i
    else:
        break
print(target)