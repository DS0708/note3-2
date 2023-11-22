x=[3, 5, 1]
y=[4, 3, 7]
z=[0, 0, 0]

for i in range(len(z)) :
    z[i] = round(x[i]/y[i],2)
    

print(z)

x.sort()

print("x정렬=",x)

# x.reverse()
x.sort(reverse=True)

print("x역정렬=",x)