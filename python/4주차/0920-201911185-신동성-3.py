'''
def getMax(n1,n2):
    if n1 == n2 :
        print(-1)
    elif n1 > n2 :
        print(n1)
    else :
        print(n2)

getMax(int(input("수1 입력: ")),int(input("수2 입력: ")))
'''

'''
def getMax(n1,n2):
    if n1 == n2 :
        return -1
    return n1 if n1 > n2 else n2

res = getMax(int(input("수1 입력: ")),int(input("수2 입력: ")))
print(res)
'''

def getMax(n1,n2):
    if n1 == n2 :
        result = -1
    elif n1 > n2 :
        result = n1
    else :
        result = n2
    return result

res = getMax(int(input("수1 입력: ")),int(input("수2 입력: ")))
print(res)
