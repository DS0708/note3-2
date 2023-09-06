'''
작성자 : 신동성
파일명 : 0906-201911185-신동성-2.py
내용 : 두 수를 입력 받아 사칙연산 결과 출력하기
'''
num1 = int(input("1st숫자:"))
num2 = int(input("2nd숫자:"))
print()
print("더하기=",num1+num2)
print("빼기=",num1-num2)
print("나머지=",num1%num2)
print("곱하기=",num1*num2)
print("나누기=",num1/num2)
print("나누기=%.2f" %(num1/num2))
print("나누기={0:.2f}".format(num1/num2))
print(f"나누기={num1/num2:.2f}")
