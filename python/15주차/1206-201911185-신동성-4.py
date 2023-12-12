search_B = [15, 20, 29, 30, 37, 55, 69, 73, 87, 90] # 순서대로 정렬
print(search_B)

key = int( input('찾으려는 값? >>> ') )
low = 0 
high = len(search_B)-1
count = 0 
find = 0 

for i in range( len(search_B) ) :
    if low <= high :
        middle = int( (low + high) / 2 )
        count += 1
        print(f'인덱스={middle}, 리스트값={search_B[middle]}')
        if key == search_B[middle] : # 검색 성공
            print(f'총 {count}번 만에 검색 성공!')
            find = 1
            break # 반복문 탈출 (검색 종료)
        elif key > search_B[middle] :
            low = middle+1 # 리스트 중앙값 수정(오른쪽 이동)
        else :
            high = middle-1 # 리스트 중앙값 수정(왼쪽으로 이동)
    if find == 0 :
        print(f'찾는 값 {key} 없음!')