arr = [70, 40, 60, 30, 10, 50]
for i in range( 1, len(arr) ) :
    key = arr[i]
    j = i-1
    while j>=0 and key<arr[j] :
        arr[j+1] = arr[j]
        j-= 1
    arr[j+1] = key
    print( i, ':', arr )