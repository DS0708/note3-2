# list
ll = [1,2,3]
print(type(ll))

# tuple
tt = (4,5,6)
print(type(tt))

# set
ss = {3,6,9}
print(type(ss))

# String
s = 'shin'
print(s)
print(s[1])

# dictionary (dict)
dd = {1:'one',2:'two'}
print(dd)
print(type(dd))

# list ex
nums = [1,2,3,4]
print(nums)
nums[0] = 5
print(nums)

nums.append(10)     
nums.insert(1,20)

print(nums)

# list ex2
nums2 = [1,[2,3],'3']
print(nums2)
print(type(nums2))

# list Function
print(sum(nums))
print(len(nums))
print(sum(nums)/len(nums))

# list index
score = [10,20,30,40]
print(score[-4])

# 내장 리스트
mix = [['jenny','chris'],['철수','영희']]
print(mix)
print(mix[0])
print(mix[1])
print(len(mix))

# in , not in
data = [1,'computer',2,'printer',['a','b']]
print(1 in data)
print('comp' in data)
print(['a','b'] in data)        #True

# list 생성
list3 = ['H','e','l','l','o']
print(list3)

list4 = list("Hello")
print(list4)

list6 = [list3,list4]
print(list6)

# pop (인덱스를 통한 삭제)
fruits = ["사과","딸기","포도"]
result = fruits.pop()
print(result)
fruits.pop(1)

print(fruits)

# remove
fruits = ["사과","딸기","포도"]
result = fruits.remove("딸기")      #remove 는 return값이 없음 , remove 는 value를 통한 삭제
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

# list 연산
word = ['a','e']
num = [1,3,5]

print(word+num)
print(word*3)

# list : index
words = ['aef','b','c','d']

print(words[0][1])

# slicing
name = ["유재석",'강호동','이경규','이수근']

print(name[0:2])
print(name[:3])
print(name[3:])
print(name[:])
print(name[1:2])
print(name[-4:-1])

# 시퀀스 자료형 len, +, *, in, not in, [], min(), max(), sum(), for 루프
print(len('slice'))
print(['s','h','i','n']+[1,2])

# range (generator)
print(range(3,5))

for i in range(2,5):
    print(i,end=" ")

print()

for i in range(4):
    print(i,end=" ")
print()

# for
str = ['hi','hello','good']
for s in str:
    print(s)









