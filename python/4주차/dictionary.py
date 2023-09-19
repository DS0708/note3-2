#list  []
num = [1,2,3,4]
print(num)
print(type(num))
# dictionary    {}
nums = {1:'one',2:'two'}
print(nums)
print(type(nums))

# creation
phone = {}
print(phone)
phone2 = dict()
print(phone2)

# insert
phone['Kim'] = "123-4567"
phone['Park'] = "234-5678"
phone['Lee'] = "344-5678"
print(phone)

# read
print(phone['Kim'])
print(phone.get('Lee'))
#print(phone[1])     #ERROR

# delete
result = phone.pop('Kim')    #value값 return
print(result)
print(phone)

# in
print('Kim' in phone)
print('Park' in phone)

# 모두 삭제
phone.clear()
print(phone)
