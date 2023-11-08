def bubble_sort(arr):
    for i in range(len(arr)-1) :
        for j in range(len(arr)-1-i) :
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]
        print(arr)
    
def select_sort(arr):
    for i in range(len(arr)-1) :
        small = i
        for j in range(i+1,len(arr)) :
            if arr[small] > arr[j] :
                small = j
        arr[small], arr[i] = arr[i], arr[small]
        print(arr)

arr = []

while True:
    user_in = input("입력할 문자는? >>> ")

    if user_in == '' :
        print(arr)
        print()
        break

    arr.append(user_in)

sel = int(input("정렬 방식? (1:버블, 2:선택) >>> "))
if sel == 1 :
    bubble_sort(arr)
elif sel == 2 :
    select_sort(arr)
else :
    print("올바른 입력 요망.")
