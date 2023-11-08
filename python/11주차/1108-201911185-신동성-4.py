#1
# main = ["샌드위치","와플","베이글"]
# sub = ["커피","주스"]

# for i in main :
#     for j in sub :
#         print(i+"+"+j)

#2
main = ["샌드위치","와플","베이글"]
sub = ["커피","주스"]
count = 1

print("<메뉴>")

for i in main :
    for j in sub :
        print(count,i+"+"+j)
        count+=1
