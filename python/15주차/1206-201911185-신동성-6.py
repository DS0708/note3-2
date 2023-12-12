arr = [40, 70, 60, 30, 10, 50]
for i in range( len(arr)-1 ) :
    small = i
    for j in range( i+1, len(arr) ) :
        if ( arr[small] > arr[j] ) :
            small = j
    arr[i], arr[small] = arr[small], arr[i]
    print( i, ':', arr )