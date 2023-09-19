E_K_dict = dict()

E_K_dict['school'] = "학교"
E_K_dict['student'] = "학생"
E_K_dict['class'] = "학급"

while(True) :
    user_input = input("단어 입력:")

    if user_input == "" :
        break
    
    print(E_K_dict.get(user_input))     #dic[word] 는 오류