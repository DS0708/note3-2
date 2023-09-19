def get_area(r):
    return 3.14*pow(r,2)

res = get_area(float(input("반지름 입력:")))
print("원의 넓이 = ",round(res,1))