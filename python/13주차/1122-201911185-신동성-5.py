knapsack = int(input("배낭 크기?"))

value = [ 10, 40, 30, 50] # 짐의가치(만원)
weight = [ 5, 4, 6, 3 ] # 짐의무게(kg)
ratio = []

print("value=",value)
print("weight=",weight)

for i in range(len(value)) :
    ratio.append([round(value[i]/weight[i],2),i])

print(ratio)

ratio.sort(reverse=True)

print(ratio)
total_value = 0
count = 0

for i in ratio :
    if knapsack == 0 :
        break

    count +=1
    if knapsack > weight[i[1]] :
        knapsack -= weight[i[1]]
    else :
        value[i[1]] *= knapsack/weight[i[1]]
        knapsack = 0
    
    total_value += value[i[1]]
    
    print(f'Round {count}. 짐 {i[1]+1} : 비율 {i[0]}, {weight[i[1]]}kg, value {value[i[1]]}만 -> 남은 공간 {knapsack}kg')
print(f'총 value = {total_value}')
    

