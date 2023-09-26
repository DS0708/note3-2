import random

user_num = int(input("수를 맞혀보세요:"))
computer_num = random.randint(1,60)

if user_num == computer_num :
    print("맞았습니다!")
elif user_num > computer_num:
    print("사용자 수가 더 큽니다.")
else :
    print("컴퓨터 수가 더 큽니다.")

print("컴퓨터 수는",computer_num,"입니다.")