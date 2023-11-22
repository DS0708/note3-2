tree = [ [5, 'a', 'b'], [2, 'a', 'g'], [2, 'a', 'c'], [1, 'b', 'c'], [7, 'b', 'e'], [9, 'e', 'f'], [4, 'c', 'f'],
[10, 'g', 'c'], [1, 'c', 'd'], [3, 'e', 'd']]

print("정렬전")
print(tree)

tree.sort()

print("정렬후")
print(tree)

shorts = []
nodes = []
total_weight = 0

for i in tree :
    if i[1] in nodes and i[2] in nodes :
        continue

    shorts.append(i)
    nodes.append(i[1])
    nodes.append(i[2])
    total_weight += i[0]

print("최소신장트리")
print(shorts)

print("정점")
print(nodes)

print()
print("가중치합 =",total_weight)