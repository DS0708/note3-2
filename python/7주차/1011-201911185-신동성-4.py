tree = ['A',
        ['B',['D','E']],
        ['C',['F','G']]
        ]
print(tree)

print('A의 왼쪽 자식 : ', tree[1][0])
print('A의 오른쪽 자식 : ', tree[2][0])
print('A의 왼쪽 자식의 자식',tree[1][1])
print('A의 오른쪽 자식의 자식',tree[2][1])
