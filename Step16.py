# #Q28278
# import sys
# n = int(sys.stdin.readline())
#
# stack = []
# for _ in range(n) :
#     o = list(map(int, sys.stdin.readline().split()))
#
#     if o[0] == 1 :
#         stack.append(o[1])
#     elif o[0] == 2 :
#         if len(stack) > 0:
#             print(stack.pop())
#         else :
#             print(-1)
#     elif o[0] == 3 :
#         print(len(stack))
#     elif o[0] == 4 :
#         if len(stack) == 0 :
#             print(1)
#         else :
#             print(0)
#     elif o[0] ==5 :
#         if len(stack) > 0 :
#             print(stack[-1])
#         else :
#             print(-1)

# #Q10773
# import sys
# k = int(sys.stdin.readline())
#
# stack = []
# for _ in range(k) :
#     n = int(sys.stdin.readline())
#     if n == 0 :
#         stack.pop()
#     else :
#         stack.append(n)
# print(sum(stack))

# #Q9012
# import sys
#
# t = int(sys.stdin.readline())
#
# for _ in range(t) :
#     s = sys.stdin.readline().strip()
#     stack = []
#     for c in s :
#         if c==')' :
#             if len(stack) == 0 :
#                 stack.append(c)
#                 break
#             elif stack[-1] == '(':
#                 stack.pop()
#             else :
#                 stack.append(c)
#         else :
#             stack.append(c)
#     if len(stack) == 0:
#         print('YES')
#     else :
#         print('NO')

#Q4949
import sys

while True :
    s = sys.stdin.readline().rstrip()
    if s == "." : break
    stack = []
    for c in s :
        if c == '[' or c =='(' :
            stack.append(c)
        elif c == ']' :
            if len(stack) != 0 and stack[-1] == '[' :
                stack.pop()
            else :
                stack.append(c)
                break
        elif c == ')' :
            if len(stack) != 0 and stack[-1] =='(' :
                stack.pop()
            else :
                stack.append(c)
                break
    if len(stack) == 0 :
        print('yes')
    else:
        print('no')


