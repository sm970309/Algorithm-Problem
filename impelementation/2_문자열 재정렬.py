s = input()
new_s = sorted(s)
sumv = 0
answer =[]
for idx,s in enumerate(new_s):
    if s.isdigit():
        sumv += int(s)
    elif s.isalpha():
        answer = new_s[idx:]
        if sumv!=0:
            answer.append(str(sumv))
        break
print(''.join(s for s in answer))