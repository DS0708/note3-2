coin = [500,100,50,10]
detail = []
change = int(input("거스름돈 금액은?"))
total = 0

for i in coin :
    count = 0
    count = change//i
    detail.append([i,count])
    change -= i*count
    total += count

print()
print(detail)

for i in detail :
    print(f'{i[0]} 원: {i[1]} 개')

print("동전 총 ",total,"개")

