import time

# 코드 실행 전의 현재 시간 기록
start_time = time.time()

# 피보나치 (recursive)
def fib(n) :
    if n == 0 :
        return 0
    elif n==1 :
        return 1
    else :
        return fib(n-1) + fib(n-2)
number = int(input("번호(인덱스) 입력: "))
answer = fib(number)
print("fibonacci = ", answer)


# 코드 실행 후의 현재 시간 기록
end_time = time.time()

# 경과 시간 계산 및 출력
elapsed_time = end_time - start_time
print(f"코드 실행에 소요된 시간: {elapsed_time} 초")

