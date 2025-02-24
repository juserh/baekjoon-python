# #Q10815
# import sys
# n = int(input())
# arr = list(map(int, sys.stdin.readline().split()))
# m = int(input())
# nums = list(map(int, sys.stdin.readline().split()))
# dic = {n: 0 for n in nums}
# for a in arr :
#     if a in dic :
#         dic[a] = 1
#
# for d in dic :
#     print(dic[d], end=" ")

# #Q14425
# n, m = map(int, input().split())
# s = set()
# for _ in range(n) :
#     s.add(input())
# cnt = 0
# for _ in range(m) :
#     i = input()
#     if i in s :
#         cnt += 1
# print(cnt)

#Q7785
n = int(input())
s = set()
for _ in range(n) :
    name, state = map(str, input().split())
    if state=="enter" :
        s.add(name)
    if state=="leave" :
        s.remove(name)
l = sorted(list(s), reverse=True)
for p in l :
    print(p)