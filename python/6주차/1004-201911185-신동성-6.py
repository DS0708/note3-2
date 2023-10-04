stk = []

while True :
    sel = int(input("선택:(1:삽입, 2:삭제, 3:종료)>>>>"))
    
    if sel == 3 :
        print("종료합니다.")
        break
    elif sel == 1 :
        val = int(input("삽입할 데이터 = "))
        stk.append(val)
        print(stk)
    elif sel == 2 :
        if len(stk) ==0 :
            print("스택이 비었습니다.")
        else :
            stk_pop = stk.pop()
            print(f'삭제된 데이터 = {stk_pop}')
            print(stk)
    