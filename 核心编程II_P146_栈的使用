# coding:utf-8
"""
核心编程II_P146。栈的使用
"""
stack = []

def pushit():
    stack.append(raw_input("Enter new string: ").strip())

def popit():
    if len(stack) == 0:
        print 'Cannot pop from an Empty stack!'
    else:
        print 'Remove [',`stack.pop()`,']'

def viewstack():
    print stack

CMDs = {'u':pushit,'o':popit,'v':viewstack}

pr = """
p(U)sh
p(O)p
(V)iew
(Q)uit
Enter choice: """

while True:
    while True:
        try:
            choice = raw_input(pr).strip().lower()
        except (EOFError,KeyboardInterrupt,IndentationError):
            choice = 'q'

        print '\nYou picked: [%s]' % choice
        if choice not in 'uovq':
            print 'Invalid option, try again'
        else:
            break
    if choice=='q':
        break

    CMDs[choice]()

if __name__ == "__main__":
    pr
