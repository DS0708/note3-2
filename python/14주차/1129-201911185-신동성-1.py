# factorial program

# num = int(input("정수 입력 :"))
# result = 1

# for i in range(1,num+1) :
#     result *= i

# print(f'{num}! = {result}')

def factorial(num) :
    result = 1
    for i in range(1,num+1) :
      result *= i
    return result
    
num = int(input("정수 입력 :"))
print(f'{num}! = {factorial(num)}')