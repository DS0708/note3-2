#
# List
#

data = [ 1, "computer", 2, "printer", [ 3, "mouse" ] ]

print( len(data) )
print( len(data[4]) )
print( data[3][2] )

print( 2 in data )
print( 2 not in data )

print( "mouse" in data )
print( [ 3, "mouse" ] in data )

fruit = ["사과", "딸기", "포도"]
print(fruit)

fruit.insert(1, '바나나')
print(fruit)

result = fruit.pop()
print(result)
print(fruit)

result = fruit.pop(0)
print(result)
print(fruit)

result = fruit.remove("딸기")
print(result)
print(fruit)

#
# Dictionary
#

phone = {}
print(type(phone))

phone = dict()
print(type(phone))

phone['Kim'] = '123'
phone['Park'] = '456'
phone['Lee'] = '789'
print(phone)

print(phone.get("Kim"))
print(phone.get("Kims"))
print(phone.get("Park"))
print(phone['Kim'])

print(phone.get("Kims"))
# print(phone['Kims'])  //ERROR

print('Kim' in phone)
print('123' in phone)

phone.clear()

print(phone)