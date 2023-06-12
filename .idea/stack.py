stack=[]

def push(self):
    element=int(input("enter the elemnt?:"))
    stack.append(element)
    print(stack)

def pop(self):
    if not stack:
        print("stack is empty!!")
    else:
        e=stack.pop()
        print("removed element:",e)
        print(stack)

while True:
    operation=int(input("enter the option: 1.push_element 2.pop_elemnt 3.quit"))
    if operation==1:
        push()
    elif operation==2:
        pop()
    else:
        print("quitted")
