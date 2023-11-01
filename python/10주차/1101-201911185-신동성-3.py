# search_L = []

# for i in range(10) :
#     input_num = int(input("입력할 수는?>>>"))
#     search_L.append(input_num)
    
# print(search_L)
# print()

# search_L.sort()

# print(search_L)

search_B = [15,20,29,30,37,55,69,73,87,90]
print(search_B)

low = 0
high = len(search_B)-1
count = 0
find = 0

key = int(input("찾으려는 값?>>"))

while low <= high :
    count +=1
    middle = (low + high) // 2
    print(f'인덱스={middle}, 리스트값={search_B[middle]}')

    if search_B[middle] == key :
        print(f"총 {count}번 만에 검색 성공!")
        find = 1
        break
    elif search_B[middle] > key :
        high = middle-1
    else :
        low = middle+1

if find == 0 :
    print(f"찾는 값 {key} 없음")