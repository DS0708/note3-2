coin = [500,100,50,10]
change = int(input("거스름돈 금액은?"))
total_coin = 0

for i in coin :
    count = 0
    count = change//i
    total_coin += count
    change -= i*count
    print(i,"원:",count,"개")

print()
print("동전 총 ",total_coin,"개")

