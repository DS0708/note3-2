# queue

num = 100
queue = []

while(True) :
    sel = int(input('1: 대기표 뽑기, 2: 업무처리, 3:종료>>>'))
    
    if sel == 1 :
        num +=1
        queue.append(num)
        print(f'대기표 번호 : {num}')
    elif sel == 2 :
        if len(queue) == 0 :
            print('큐가 비었습니다.')
        else :
            del_data = queue.pop(0) 
            print(f'업무처리 번호 : {del_data}')
    elif sel == 3 :
        print("종료합니다.")
        break
