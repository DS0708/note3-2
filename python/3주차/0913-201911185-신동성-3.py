# 실습 3 (for)

'''
for i in range(3):
    print("안녕")
'''

#1~10
'''
for i in range(1,11):
    print(i)
'''

#10~1
'''
for i in range(10,0,-1):
    print(i)
'''

# 입력받은 값 까지 출력하기
'''
n = int(input("숫자 입력:"))
for i in range(1,n+1):
    print(i)
'''

# 입력받은 값 까지 홀수만 출력하기
'''
n = int(input("숫자 입력:"))
for i in range(1,n+1,2):
    print(i)
'''

# 팩토리얼 계산하기
n = int(input("정수 입력:"))
res = 1
for i in range(1,n+1):
    res *= i
print("%d! = %d" %(n,res))