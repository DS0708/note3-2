arr = [70, 40, 60, 30, 10, 50]

print(arr)

for i in range(1, len(arr)):
    j = i-1
    key = arr[i]
    while j>=0 and key < arr[j] :
        arr[j+1] = arr[j]
        j -=1
    arr[j+1] = key
    print(i,':',arr)
    
print(arr)