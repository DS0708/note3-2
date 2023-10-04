def SimpleLinkedList(A,root):
    head = root
    next = head

    while next != None :
        value = A[next][0]
        next = A[next][1]
        print(value,next)

# Main
nums = {8:[65,4],4:[54,9],9:[12,None]}
print(nums)
print(nums[8])
print(nums[8][0])
print(nums[8][1])

SimpleLinkedList(nums,8)
