# 실습 6
n = int(input("수 입력:"))
print("1~%d까지 3의 배수" %(n))

# continue 사용하지 않은 code
i = 1
while (i <= n):
    if(i%3)==0:
        print(i)
    i = i+1

# continue 사용 code
'''
count = 0
while (count <= n):
    count+=1
    if count % 3 == 0 :
        print(count)
    else :
        continue
'''