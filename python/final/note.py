##### 이진 검색 #####

# search_B = [15, 20, 29, 30, 37, 55, 69, 73, 87, 90] # 순서대로 정렬
# print(search_B)

# high = len(search_B)-1
# low = 0
# count = 0
# key = int(input('찾으려는 값? >>>'))

# for i in range(len(search_B)) :
#     middle = (high + low )//2
#     count +=1
#     print(f'인덱스={middle}, 리스트값={search_B[middle]}')
#     if key == search_B[middle] :
#         print()
#         print(f'총 {count}번 만에 검색 성공!')
#         break
#     elif key > search_B[middle] :
#         low = middle + 1
#     else :
#         high = middle - 1
    
#     if high < low :
#         print()
#         print(f'찾는 값 {key} 없음!')
#         break

##### 버블 정렬 #####
# li = []
# while (True) :
#     data = int(input('입력할 수는? >>>'))
#     if data < 0 :
#         break
#     else :
#         li.append(data)

# for i in range(len(li)-1) :
#     for j in range(len(li)-i-1) :
#         if li[j] > li[j+1] :
#             li[j], li[j+1] = li[j+1], li[j]
#     print(f'{i}:{li}') 


##### 선택 정렬 #####
# arr = [40, 70, 60, 30, 10, 50]
# for i in range(len(arr)-1) :
#     small = i
#     for j in range(i,len(arr)-1) :
#         if arr[small] > arr[j] :
#             small = j
#     arr[small], arr[i] = arr[i], arr[small]
#     print(f'{i}:{arr}')

#### 삽입 정렬 ####
# arr = [70, 40, 60, 30, 10, 50]
# for i in range(1,len(arr)) :
#     key = arr[i]
#     j = i - 1
#     while j >= 0 and arr[j] > key :
#         arr[j+1] = arr[j]
#         j -= 1
#     arr[j+1] = key
#     print(f'{i}:{arr}')

#### 거스름돈 문제 ####
# coins = [500,100,50,10]
# coins_num = []
# money = int(input('거스름돈 얼마?'))
# total = 0

# for i in range(len(coins)) :
#     num = money//coins[i]
#     money -= coins[i]*num
#     coins_num.append([coins[i],num])
#     total += num

# print(coins_num)
# for i in coins_num :
#     print(f'{i[0]} 원 : {i[1]}개')
# print(f'동전 총 {total}개')

#### 피보나치 재귀 함수 ####
# def fibonazzi(n):
#     if n == 1 :
#         return 1
#     elif n == 0 :
#         return 0
#     else :
#         return fibonazzi(n-1) + fibonazzi(n-2)

# index = int(input('번호(인덱스) 입력 : '))
# print(fibonazzi(index))

#### 피보나치 다이나믹 프로그래밍 ####
def fib(n):
    fin_arr=[0,1]
    for i in range(2,n+1):
        fin_arr.append(fin_arr[i-1]+fin_arr[i-2])
    return fin_arr[n]

num = int(input("번호(인덱스) 입력:"))
print(fib(num))


