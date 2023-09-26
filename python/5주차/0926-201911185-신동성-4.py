list_1 = list()
list_2 = ["시간","사랑","가나다라"]

for i in range(3) :
    user_in = input("원하는 단어를 입력하세요>> ")
    list_1.append(user_in)

print("리스트1 = ",list_1)
print("리스트1 + 리스트2 = ",list_1[1]+list_2[1])