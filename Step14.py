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

# #Q7785
# n = int(input())
# s = set()
# for _ in range(n) :
#     name, state = map(str, input().split())
#     if state=="enter" :
#         s.add(name)
#     if state=="leave" :
#         s.remove(name)
# l = sorted(list(s), reverse=True)
# for p in l :
#     print(p)

# #Q1620
# import sys
# n, m = map(int, sys.stdin.readline().split())
# dic = {}
# for i in range(n) :
#     name = sys.stdin.readline().strip()
#     dic[name] = i+1
#
# swap = dict(zip(dic.values(), dic.keys())) #key-value 스왑한 딕셔너리
# for _ in range(m) :
#     p = sys.stdin.readline().strip()
#     if p.isnumeric() :
#         print(swap[int(p)])
#     else :
#         print(dic[p])

# #Q10816
# import sys
# n = int(sys.stdin.readline().strip())
# arr = list(map(int, sys.stdin.readline().split()))
# m = int(sys.stdin.readline().strip())
# nums = list(map(int, sys.stdin.readline().split()))
#
# dic={}
# for a in arr :
#     if a in dic :
#         dic[a] += 1
#     else :
#         dic[a] =1
#
# for num in nums :
#     if num in dic :
#         print(dic[num], end= " ")
#     else :
#         print(0, end=" ")

# #Q1764
# n, m = map(int, input().split())
# nh = set()
# ns = set()
# for _ in range(n) :
#     name = input()
#     nh.add(name)
#
# for _ in range(m) :
#     name = input()
#     ns.add(name)
#
# print(len(nh&ns))
# for name in sorted(nh&ns) :
#     print(name)

#Q1269
n, m = map(int, input().split())
a = set(map(int, input().split()))
b = set(map(int, input().split()))

print(len(a-b)+len(b-a))