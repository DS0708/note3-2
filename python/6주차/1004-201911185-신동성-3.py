# num = list()
# print(num)
# for i in range(4) :
#     num.append(int(input("추가할 값은? ")))

# print(num)

# num.insert(2,12)

# print(num)

num = [1,2,3,4,5]
print(num)

while True :
    sel = input("원하는 인덱스 번호는? ")
    if sel == ' ' :
        print("종료...")
        break
    
    val = int(input(f'인덱스 [{sel}] 위치에 추가할 값은 ?'))

    num.insert(int(sel),val)
    print(num)