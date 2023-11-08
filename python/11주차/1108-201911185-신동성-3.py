#1
# dan = int(input("몇 단?"))

# for i in range(1,10):
#     print(f'{dan} * {i} = {dan*i}')

#2
for i in range(2,10) :
    for j in range(1,10) :
        print("%2d * %2d = %2d" %(i,j,i*j))
    if i != 9 :
        print()