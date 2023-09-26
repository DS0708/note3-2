game = dict()

for i in range(3) :
    item_name = input("구매할 게임 아이템은? ")
    item_num = int(input("개수는 몇 개?"))
    game[item_name] = item_num

print()
print("구매한 게임 아이템 = ", game)
print()
print("딕셔너리에 구매한 아이템이 있는지 확인하세요.")
is_item = input("확인하고 싶은 아이템은? ")

if is_item in game :
    print(f'{is_item}은(는) {game[is_item]}개 있습니다')
else :
    print(f'{is_item}은(는) 없습니다')
