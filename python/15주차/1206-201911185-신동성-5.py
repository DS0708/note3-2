arr = [] 
while True :
    num = int(input("입력할 수는? >>> "))
    if num < 0 :
        break
    arr.append(num)
for i in range( len(arr)-1 ) :
    for j in range( len(arr)-1 - i ) :
        if ( arr[j] > arr[j+1] ) :
            arr[j], arr[j+1] = arr[j+1], arr[j]
    print( i, ':', arr )