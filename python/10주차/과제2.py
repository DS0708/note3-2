num_list = []

while True :
    list_input_num = int(input("입력할 수는?>>>")) 
    if list_input_num < 0 :
        break
    num_list.append(list_input_num)

print(num_list)
num_list.sort()
print(num_list)

key = int(input("찾으려는 값? >>>"))

low = 0
high = len(num_list)-1
for i in range(len(num_list)) :
    if low > high :
        print(f'찾는 값 {key} 없음!')
        break
    
    middle = (high+low) //2

    print(f'인덱스={middle}, 리스트값={num_list[middle]}')

    if num_list[middle] == key :
        print(f'총 {i+1}번 만에 검색 성공!')
        break
    elif num_list[middle] > key :
        high = middle - 1
    else :
        low = middle + 1