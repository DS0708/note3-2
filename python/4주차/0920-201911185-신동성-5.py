# def area(w,h):
#     result = w*h
#     return result

# width = 10
# height = 20
# result = 0

# print("면적 = ",area(width,height))
# print(result)

def area(w,h):
    global result
    result = w*h
    return result

width = 10
height = 20
#result = 0     #안써도됨

print("면적 = ",area(width,height))
print(result)

