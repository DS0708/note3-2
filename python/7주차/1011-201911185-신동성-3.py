g_dict = { 'A':['B','C'],
          'B':['A','E'],
          'C':['A','D','E'],
          'D':['C','E'],
          'E':['B','C','D'],
          }

while True :
    sel = input("확인하려는 정점? ")

    if sel == '' :
        break
    else :
        print(g_dict.get(sel)) 