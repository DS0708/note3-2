# def recur() :
#     print("재귀함수")
# recur()



# recursive factorial
def factorial(num) :
    if(num<=0) :
        print("바른 입력 요망")
        exit()

    if num == 1 :
        return num
    else :
        return num*factorial(num-1) 

    
num = int(input("정수 입력 :"))
print(f'{num}! = {factorial(num)}')

