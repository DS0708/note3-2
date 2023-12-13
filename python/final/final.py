# Stack

# stk=[]

# while(True):
#     sel = int(input('선택 (1:삽입, 2:삭제, 3:종료) >>>'))

#     if sel == 1 :
#         data = int(input('삽입할 데이터 = '))
#         stk.append(data)
#         print(stk)
#     elif sel == 2 :
#         if len(stk) == 0 :
#             print('스택이 비었습니다.')
#         else :
#             print(f'삭제된 데이터 = {stk.pop()}')
#             print(stk)
#     elif sel ==3 :
#         print('종료합니다.')
#         break

# queue

# num = 100
# queue = []

# while(True):
#     sel = int(input('1: 대기표 뽑기, 2: 업무처리, 3:종료>>>'))
#     if sel == 1 :
#         num+=1
#         queue.append(num)
#         print(f'대기표 번호 : {num}')
#     elif sel == 2 :
#         if len(queue) == 0 :
#             print(f'큐가 비었습니다.')
#         else :
#             print(f'업무처리 번호 : {queue.pop(0)}')
#     elif sel == 3 :
#         print('종료합니다.')
#         break

# Linear Search
# arr = []

# while (True) :
#     data = int(input('입력할 수는? >>>'))
#     if data < 0 :
#         break
#     else :
#         arr.append(data)

# print(arr)
# print()

# key = int(input('찾고자 하는 수는? >>>'))
# find = 0

# for i in range(len(arr)) :
#     print(f'index{i} : {arr[i]}')
#     if key == arr[i] :
#         print(f'인덱스{i}에서 검색 성공 !~')
#         find = 1
#         break

# if find == 0 :
#     print('찾는 값 없음 !')


# Binary search
# search_B = [15, 20, 29, 30, 37, 55, 69, 73, 87, 90]
# print(search_B)

# key = int(input('찾으려는값? >>> '))
# find = 0
# high = len(search_B) - 1
# low = 0
# count = 0

# for i in range(len(search_B)):
#     middle = (high+low)//2
#     count +=1
#     print(f'인덱스{middle}, 리스트값={search_B[middle]}')
#     if key == search_B[middle] :
#         print(f'총 {count}번 만에 검색 성공!')
#         find = 1
#         break
#     elif key > search_B[middle] :
#         low = middle + 1
#     else :
#         high = middle - 1
    
#     if low > high :
#         break

# if find == 0 :
#     print(f'찾는 값 {key}없음 !')

# Bubble Sort
# arr = []

# while(True):
#     data = int(input('입력할 수는 ? >>>'))
#     if data < 0 :
#         break
#     else :
#         arr.append(data)

# for i in range(len(arr)-1):
#     for j in range(len(arr)-1-i):
#         if arr[j] > arr[j+1] :
#             arr[j], arr[j+1] = arr[j+1], arr[j]
#     print(f'{i}:{arr}')

# Select Sort
# arr = [40, 70, 60, 30, 10, 50]

# for i in range(len(arr)-1):
#     small = i
#     for j in range(i+1,len(arr)):
#         if arr[small] > arr[j] : 
#             small = j
#     arr[small], arr[i] = arr[i], arr[small]
#     print(f'{i}:{arr}')
    
# Insert Sort
# arr = [70, 40, 60, 30, 10, 50]

# for i in range(1,len(arr)):
#     key = arr[i]
#     j = i - 1
#     while j >=0 and arr[j] > key :
#         arr[j+1] = arr[j]
#         j -= 1
#     arr[j+1] = key
#     print(f'{i}:{arr}') 

# 거스름돈 문제
# coin = [500,100,50,10]
# coin_arr = []
# money = int(input('거스름돈 얼마?'))
# total_coin = 0

# for i in range(len(coin)):
#     coin_num = money//coin[i]
#     coin_arr.append([coin[i],coin_num])
#     money -= coin[i]*coin_num
#     total_coin += coin_num

# print(coin_arr)

# for i in coin_arr:
#     print(f'{i[0]} 원 : {i[1]} 개')

# print(f'동전 총 {total_coin}')

# 피보나치 재귀
# def fib_re(n):
#     if n == 1 :
#         return 1
#     elif n ==0 :
#         return 0
#     else :
#         return fib_re(n-1) + fib_re(n-2)

# index = int(input('번호(인덱스)입력:'))
# print(f'fibonacci = {fib_re(index)}')

# 피보나치 다이나믹 프로그래밍
def fib_dy(n):
    fib_arr = [0,1]
    for i in range(2,n+1) :
        fib_arr.append( fib_arr[i-1] + fib_arr[i-2])
    return fib_arr[n]

index = int(input('번호(인덱스)입력:'))
print(f'fibonacci = {fib_dy(index)}')