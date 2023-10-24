num = int(input("정수 입력:"))

i = 1
sum = 0
nums = []

while i <= num :
    nums.append(i)
    i += 1

for i in nums :
    sum += i


print(f'합 = {sum}')