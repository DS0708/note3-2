a = 3   #Global variable

def plus(num) :
    b = num + a #Local variable
    #a = 7      전역변수 값을 함수에서 바꿀 수 없다.
    return b

print(plus(5))
print(a)

###############
###############
###############
###############
###############
###############

def plus(num) :
    global b   #함수 안에서 Global variable 명시적 선언     
    print(b)    #2
    b = num + a #Local variable
    print(b)                #3
    return b


b = 1
a = 3   #Global variable

print(b)    # 1

print(plus(5))  #4

print(b)    #5
###############
def change():
    global x
    x = 5
    y=6
    global z
    z = 7

x=1
y=2

change()

print(x,y,z)

###############
def sub():
    global s
    print(s)      #global s  없으면 에러        
    s="banana"
    print(s)

s = "apple"

sub()

print(s)