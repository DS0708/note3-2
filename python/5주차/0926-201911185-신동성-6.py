def func_1 (list) :
    for i in list :
        if i == 12 :
            print("\n12 확인! 반복을 종료합니다.")
            return
        print(i,end=" ")
    print()

num1 = [1,2,3,[4,5],6,[7]]
num2 = [1,2,3,[4,5],12,6,[7]]  

func_1(num1)
func_1(num2)