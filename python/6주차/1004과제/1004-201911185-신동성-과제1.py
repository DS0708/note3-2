def enqueue(data) :
    ticket_queue.append(data)
def dequeue() :
    if len(ticket_queue) == 0 :
            print("큐가 비었습니다.")
    else :
        res = ticket_queue.pop(0)
        return res

ticket_queue = []
ticket_count = 100

while True :
    sel = int(input("1:대기표 뽑기, 2:업무처리, 3:종료>>>"))
    if sel ==1 :
        ticket_count +=1
        enqueue(ticket_count)
        print(f'대기표 번호:{ticket_count}')
    elif sel ==2 :
        res = dequeue()
        if res != None :
            print(f'업무처리 번호:{res}')
    elif sel ==3 :
        print("종료합니다.")
        break
    else :
        print("재입력 요망")