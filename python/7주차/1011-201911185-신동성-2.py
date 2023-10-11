g_array = [[0,1,1,0,0],
           [1,0,0,0,1],
           [1,0,0,1,1],
           [0,0,1,0,1],
           [0,1,1,1,0],
           ]

vertic1 = int(input("정점1의 번호? "))
vertic2 = int(input("정점2의 번호? "))

if g_array[vertic1][vertic2] == 1 :
    print(f'정점 {vertic1},{vertic2} : 인접')
else :
    print(f'정점 {vertic1},{vertic2} : 인접아님')


