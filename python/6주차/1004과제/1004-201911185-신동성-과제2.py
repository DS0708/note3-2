# P.336 도전문제1. 스택
'''
#Function
def push(data):
    global stk
    stk.append(data)
def pop():
    global stk
    if len(stk) !=0 :
        return stk.pop()
    else :
        print("Stack is empty.")

# Main
stk = []

for i in range(6) :
    push(input("Input the character to insert into the stack :"))

for i in range(6) :
    print(pop(),end='')
print()
'''

# P.337 도전문제2. 연결 리스트

#Function
def addToLinkedList(data):
    global list_count  
    global linked_list  
    current = linked_list[0]

    while True:
        if current[1] is None:
            current[1] = list_count
            linked_list[list_count] = [data, None]
            list_count += 1
            break
        else:
            current = linked_list[current[1]]

def printLinkedList():
    global list_count  
    global linked_list 
    current = linked_list[0]

    while True:
        if current[0] != "Root" : 
            print(current[0],end='')
        if current[1] is None :
            break
        current = linked_list[current[1]]
    print()
# Main
list_count = 1
linked_list = {0: ["Root", None]}

for i in range(6) :
    addToLinkedList(input("Input the character to insert into the linked_list :"))

printLinkedList()
