# 실습4 (while)
count = 0

'''
while(count < 4):
    print("안녕")
    count+=1
'''

# 1~10
'''
while(count<10):
    print(count+1)
    count+=1
'''

# 10~1
'''
count +=10

while(count>0):
    print(count)
    count -=1
'''

# 입력받은 값 까지 출력하기
'''
count = 1
n = int(input("숫자 입력:"))
while (count <=n ):
    print(count)
    count+=1
'''

# 입력받은 값 까지 홀수만 출력하기
'''
count = 1
n = int(input("숫자 입력:"))
while (count <=n ):
    print(count)
    count+=2
'''

# 팩토리얼 계산하기
n = int(input("정수 입력:"))
res = 1
count = 1
while (count <= n):
    res *= count
    count+=1
print("%d! = %d" %(n,res))

