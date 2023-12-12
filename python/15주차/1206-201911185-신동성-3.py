# 선형 검색

li = []

while(True):
    in_data = int(input('입력할 수는? >>> '))
    if in_data < 0 :
        break
    li.append(in_data)

key = int(input('찾고자 하는 수는? >>>'))

for i in range(len(li)) :
    print(f'index{i} : {li[i]}')

    if key == li[i] :
        print(f'인덱스 [{i}]에서 검색 성공 !')
        break
    
    if i == len(li)-1 :
        print('찾는 값 없음!')
