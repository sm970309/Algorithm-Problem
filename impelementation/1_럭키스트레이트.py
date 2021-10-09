n = input()
left = list(map(int,n[:len(n)//2]))
right = list(map(int,n[len(n)//2:]))

if sum(left)==sum(right):
    print("LUCKY")
else:
    print("READY")
