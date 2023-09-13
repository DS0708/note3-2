# 실습 7

vowels = ['a','e','i','o','u']

str = input('문자열 입력:')

for s in str:
    if s in vowels:
        print(s, end=" ")
