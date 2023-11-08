#1
# for i in "abcde" :
#     print(i,end="")
#     for j in "01234":
#         print(j,end="")
#     print()

#2
# for i in "abcde" :
#     for j in "01234":
#         print(j,end="")
#     print(i,end="")
#     print()

#3
for i in range(1,6) :
    for j in range(1,i+1) :
        print("*",end="")
    print()