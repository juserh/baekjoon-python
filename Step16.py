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

# #Q4949
# import sys
#
# while True :
#     s = sys.stdin.readline().rstrip()
#     if s == "." : break
#     stack = []
#     for c in s :
#         if c == '[' or c =='(' :
#             stack.append(c)
#         elif c == ']' :
#             if len(stack) != 0 and stack[-1] == '[' :
#                 stack.pop()
#             else :
#                 stack.append(c)
#                 break
#         elif c == ')' :
#             if len(stack) != 0 and stack[-1] =='(' :
#                 stack.pop()
#             else :
#                 stack.append(c)
#                 break
#     if len(stack) == 0 :
#         print('yes')
#     else:
#         print('no')

# #Q12789
# import sys
# n = int(sys.stdin.readline())
# arr = list(map(int, sys.stdin.readline().split())) #FIFO
# sub = [] #stack
#
# nxt = 1
# for a in arr :
#     sub.append(a)
#
#     while sub and sub[-1] == nxt :
#         sub.pop()
#         nxt += 1
#
# if sub :
#     print("Sad")
# else :
#     print("Nice")

# #Q18258
# from collections import deque
# import sys
#
# n = int(sys.stdin.readline())
# q = deque([])
# for _ in range(n) :
#     s = list(map(str, sys.stdin.readline().split()))
#
#     if s[0] == "push" :
#         x = int(s[1])
#         q.append(x)
#     elif s[0] == "pop" :
#         if q :
#             print(q.popleft())
#         else :
#             print(-1)
#     elif s[0] == "size" :
#         print(len(q))
#     elif s[0] == "empty" :
#         if q :
#             print(0)
#         else :
#             print(1)
#     elif s[0] == "front" :
#         if q :
#             print(q[0])
#         else :
#             print(-1)
#     elif s[0] == "back" :
#         if q :
#             print(q[-1])
#         else :
#             print(-1)

# #Q2164
# from collections import deque
# import sys
#
# n = int(sys.stdin.readline())
# que = deque([i for i in range(1, n+1)])
#
# while len(que) > 1 :
#     que.popleft()
#     last = que.popleft()
#     que.append(last)
# print(que.pop())

#Q11866
import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())
que = deque([ i for i in range(1, n+1)])

out = []
while len(que)>0 :
    for _ in range(k-1) :
        que.append(que.popleft())
    out.append(str(que.popleft()))

print('<'+', '.join(out)+'>')