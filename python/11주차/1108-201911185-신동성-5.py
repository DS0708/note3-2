# arr = [40, 70, 60,30,10,50]
arr = [4,7,6,3,1,5]
print(arr)
for i in range(len(arr)-1) :
    for j in range(len(arr)-i-1) :
        if arr[j] > arr[j+1] :
            arr[j], arr[j+1] = arr[j+1], arr[j]
    print(i,":",arr)