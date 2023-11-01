search_B = [15,20,29,30,37,55,69,73,87,90]
print(search_B)

low = 0
high = len(search_B) - 1
key = int(input("찾으려는 값?>>"))

print()
for i in range(len(search_B)) :

    if low > high :
        print()
        print(f'찾는 값 {key} 없음 !')
        break

    middle = (low+high) // 2

    print(f'인덱스={middle}, 리스트값={search_B[middle]}')

    if search_B[middle] == key :
        find = 1
        print()
        print(f'총 {i+1}번 만에 성공!')
        break
    elif search_B[middle] < key :
        low = middle + 1
    else :
        high = middle - 1

