import time

# 코드 실행 전의 현재 시간 기록
start_time = time.time()

# 피보나치 (점화식)
def fib(n) :
    if n==0 or n==1 :
        return n
    elif n >=2 :
        x, y = 0, 1
        for i in range(n-1) :
            x , y = y, x+y
        return y
number = int(input("번호(인덱스) 입력 : "))
answer = fib(number)
print("fibonacci =", answer)

# 코드 실행 후의 현재 시간 기록
end_time = time.time()

# 경과 시간 계산 및 출력
elapsed_time = end_time - start_time
print(f"코드 실행에 소요된 시간: {elapsed_time} 초")

