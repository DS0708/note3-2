search_L = []
i = 0

while True :
    input_num = int(input("입력할 수는?>>>"))
    
    if input_num < 0 :
        break
    else :
        search_L.append(input_num)

print(search_L)
key = int(input("찾고자 하는 수는?>>>"))
print()

while True :
    print(f'index{i} : {search_L[i]}')
    if search_L[i] == key :
        print()
        print(f'인덱스[{i}]에서 검색 성공!')
        break
    elif i == len(search_L)-1 :
        print(f'찾는 값 없음!')
        break
    
    i+=1
