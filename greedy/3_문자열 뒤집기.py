s = input()
def make_0(s):
    count = 0
    if s[0] == "1":
        count += 1
    for i in range(len(s)-1):
        if s[i]=="0" and s[i+1]=="1":
            count += 1
    return count
def make_1(s):
    count = 0
    if s[0] == "0":
        count += 1
    for i in range(len(s)-1):
        if s[i]=="1" and s[i+1]=="0":
            count += 1
    return count

print(min(make_1(s),make_0(s)))