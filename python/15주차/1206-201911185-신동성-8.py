coin = [500, 100, 50, 10]
cnt = 0
detail = []

money = int( input('거스름돈 금액은? ') )

for i in coin :
    num = money // i
    cnt += num
    money = money- ( num * i )
    detail.append( [i, num] )

print( detail )

for i in detail :
    print( i[0], '원 : ', i[1], '개' )

print( '동전 총', cnt,'개')