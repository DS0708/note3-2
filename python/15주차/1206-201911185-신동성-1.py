# Stack

stk = []

while(True) :
    sel = int(input("선택 (1:삽입, 2:삭제, 3:종료) >>>"))
    
    if sel == 1 :
      input_data = int(input("삽입할 데이터 = "))
      stk.append(input_data)
      print(stk)
    elif sel == 2 :
      if len(stk) != 0 :
        del_data = stk.pop()
        print(f'삭제된 데이터 = {del_data}')
        print(stk)
      else :
        print('스택이 비었습니다.')
    elif sel ==3 :
      print('종료합니다.')
      break

