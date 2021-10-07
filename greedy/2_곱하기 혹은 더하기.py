nums = input()
answer = 0
for num in nums:
    num = int(num)
    if answer == 0:
        answer += num
    else:
        if num<=1:
            answer += num
        else:
            answer *= num
print(answer)