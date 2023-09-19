'''
def plus(num) :
    print(b)    
    b = num + a 
    print(b)                
    return b

b = 1
a = 3   

print(b)    

print(plus(5))  

print(b)    
'''


def plus(num) :
    global b   #local b 를 생성하는 것이 아닌 Global b 를 사용하겠다는 표시, Global b가 없을 시 ERROR     
    print(b)    #2
    b = num + a #Local variable
    print(b)                #3
    return b

b = 1
a = 3   #Global variable

print(b)    # 1

print(plus(5))  #4

print(b)    #5
