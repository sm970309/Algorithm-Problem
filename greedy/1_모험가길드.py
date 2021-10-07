n = int(input())
data = list(map(int,input().split()))
data.sort(reverse=True)
print(data)
count = 0
i = 0
while True:
    count += 1
    i += data[i]
    if i>=n:
        break
print(count)