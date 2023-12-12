def fib_dp(n):
    fib_m = [0,1]

    for i in range(2, n+1) :
        num = fib_m[i-1] + fib_m[i-2]
        fib_m.append(num)
    return fib_m[n]

number = int(input("번호(인덱스) 입력 : "))
answer = fib_dp(number)
print("fibonacci =", answer)