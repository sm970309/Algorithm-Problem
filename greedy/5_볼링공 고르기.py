from itertools import combinations
n,m = map(int,input().split())
k = list(map(int,input().split()))

k.sort()
x = len(k)-len(set(k))
new_list = list(combinations(k,2))
print(len(new_list) - x)