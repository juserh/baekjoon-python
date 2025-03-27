#Q28278
import sys
n = int(sys.stdin.readline())

stack = []
for _ in range(n) :
    o = list(map(int, sys.stdin.readline().split()))

    if o[0] == 1 :
        stack.append(o[1])
    elif o[0] == 2 :
        if len(stack) > 0:
            print(stack.pop())
        else :
            print(-1)
    elif o[0] == 3 :
        print(len(stack))
    elif o[0] == 4 :
        if len(stack) == 0 :
            print(1)
        else :
            print(0)
    elif o[0] ==5 :
        if len(stack) > 0 :
            print(stack[-1])
        else :
            print(-1)