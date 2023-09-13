# 실습 2번

'''
# pop   (delete by index)
fruits = ["사과","딸기","포도"]
result = fruits.pop()
print(result)
fruits.pop(1)

print(fruits)

# remove (delete by value)
fruits = ["사과","딸기","포도"]
result = fruits.remove("딸기")      #remove 는 return값이 없음 
print(result)
print(fruits)

# reverse, sort, insert, append, count, index
fruits = ["사과","딸기","포도"]

fruits.reverse()
print(fruits)

fruits.sort()
print(fruits)

fruits.insert(1,'바나나')

fruits.append('바나나')
print(fruits)

print(fruits.count('바나나'))

print(fruits.index('바나나'))       #2개일때 첫번재 Index값 출력
'''

# list : index
words = ['aef','b','c','d']

print(words[0][1])

# slicing
name = ["유재석",'강호동','이경규','이수근']

print(name[0:2])
print(name[:3])
print(name[3:])
print(name[:])