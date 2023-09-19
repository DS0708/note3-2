# 함수는 정의 후 사용해야함
def get_sum(num1,num2) :
    sum = 0
    for i in range(num1,num2+1) :
        sum += i
    return sum

value = get_sum(1,10)
print(value)

def swap(a,b) :
    temp = a
    a = b
    b = temp
    return

x = 10
y = 11
print(swap(x,y))
print (x , y)       # 얕은 복사가 되는듯