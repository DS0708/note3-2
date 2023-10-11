tree_dict = {'A':['B','C'],'B':['D','E'],'C':['F','G']}

print(tree_dict)

for i in tree_dict :
    print(f'{i}의 자식 : {tree_dict.get(i)}')
