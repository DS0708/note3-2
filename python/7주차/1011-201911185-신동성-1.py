# 딕셔너리
print("---------dict--------")
print()
phone = {}
print(phone)

phone['Kim'] = "123-4567"
phone['Park'] = "234-5678"
phone['Lee'] = "345-6789"
print(phone)

#Search by Key
print(phone['Kim'])
print(phone.get('Lee'))

# 리스트
print()
print("---------list--------")
print()

data = [ 1, "computer", 2, "printer", [ 3, "mouse" ] ] #혼합자료형
print(data[3])
print(data[3][2]) 
print(data[4][1])
print(data[4][1][0])