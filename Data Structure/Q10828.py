def push(x, l) :
    l.append(x)
def pop(l) :
    if len(l) == 0 :
        print(-1)
    else :
        print(l.pop())
def size(l) :
    return print(len(l))
def empty(l) :
    if len(l) == 0 : print(1)
    else: print(0)
def top(l) :
    if len(l) == 0 : print(-1)
    else : print(l[-1])

import sys
n = int(sys.stdin.readline())
stack = list()
for _ in range(n) :
    o= list(map(str, sys.stdin.readline().split()))
    if 'push' in o:
        x = int(o[1])
        push(x, stack)
    elif 'pop' in o:
        pop(stack)
    elif 'size' in o:
        size(stack)
    elif 'empty' in o:
        empty(stack)
    elif 'top' in o:
        top(stack)